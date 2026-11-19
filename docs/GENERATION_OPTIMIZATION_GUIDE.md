# Model Generation & GPU Optimization Guide

This guide covers running large reasoning models (such as `deepseek-r1:32b`), troubleshooting empty answer errors caused by token constraints, understanding pipeline execution logs, and maximizing throughput on NVIDIA GPUs.

---

## 1. Canonical Generation Command (DeepSeek-R1 32B)

To run generation for `deepseek-r1:32b`, execute the following from the repository root:

```bash
.venv/bin/python scripts/run_campaign.py generate \
  --model deepseek-r1:32b \
  --working checkpoints/campaign_deepseek-r1_32b_working.jsonl \
  --output data/campaign_deepseek-r1_32b.jsonl
```

- **Checkpointing:** Generation is append-only and resumable. If stopped or interrupted, re-running the exact same command continues from where it stopped.
- **Single-Model Isolation:** Running `--model deepseek-r1:32b` pins model weights in GPU VRAM without thrashing between different model architectures.

---

## 2. Problem: Why DeepSeek-R1 (and other 32B models) Fail on `max_tokens`

### Observed Error Trace

```text
[campaign 25/5000] english/missing/bm25/deepseek-r1:32b
Traceback (most recent call last):
  ...
  File "src/banglarag_eval/pipeline/campaign.py", line 1766, in generate_record
    raise RuntimeError(
RuntimeError: generation failed three times for c50kv3u-007-code-part-1a77c5: generator returned an empty answer
```

### Technical Root Cause

1. **Reasoning Models Always Output Thinking Traces:**
   DeepSeek-R1 is a reinforcement-learning-trained reasoning model. Unlike standard LLMs (Gemma, Llama, Qwen with `/no_think`), DeepSeek-R1 **cannot disable its internal chain of thought**. It unconditionally emits an internal reasoning trace enclosed in `<think> ... </think>` tags before generating its answer.
2. **Token Starvation with `max_tokens: 256`:**
   In `configs/campaign_50000_v3_unreviewed.yaml`, the default decoding setting is `max_tokens: 256`. 
   A typical DeepSeek-R1 reasoning process takes **200 to 350 tokens**.
   When capped at 256 tokens:
   - DeepSeek-R1 consumes all 256 tokens entirely inside `<think>` or immediately as the tag closes.
   - Ollama halts generation (`finish_reason: length`, `truncated: True`).
   - **Zero tokens** remain for the actual final answer text.
3. **Empty Answer Stripping:**
   The pipeline's `_strip_thinking()` function cleanly removes `<think> ... </think>` so reasoning traces do not pollute evaluation data. Because the model was cut off at the tag boundary, the remaining answer string is `""` (empty string).
4. **Validation Tripwire:**
   The campaign runner enforces `if not result.answer.strip(): raise RuntimeError("generator returned an empty answer")`. After three retries, the entire run halts.

---

## 3. Solution Guide

### Increase `max_tokens` to 512 or 768

In `configs/campaign_50000_v3_unreviewed.yaml`, adjust `generation.max_tokens`:

```yaml
generation:
  temperature: 0.0
  max_tokens: 512          # Increased from 256 to allow reasoning headroom
  prompt_version: rag_campaign_concise_v3
```

### Empirical Verification

Testing the exact failing scenario (`c50kv3u-007-code-part-1a77c5`) with `max_tokens: 512`:

```text
eval_count: 270 tokens
finish_reason: stop
truncated: False
Parsed answer: 'The context does not provide sufficient information to answer the question.'
```

DeepSeek-R1 required **250 tokens** to think and **20 tokens** to provide its answer. With `max_tokens: 512`, generation completes with `finish_reason: stop` and succeeds cleanly.

> [!NOTE]
> Raising `max_tokens` to 512 does **not** make standard models (e.g. `gemma3:4b`, `llama3.2:3b`) generate longer or slower outputs. Non-reasoning models terminate upon reaching the EOS token (typically in 20–50 tokens). It only expands the maximum headroom for reasoning models.

---

## 4. Understanding Campaign Logs: Why All Status Logs Say `english/missing`

During generation, you will observe log lines formatted like:

```text
[campaign 25/5000] english/missing/bm25/deepseek-r1:32b
[campaign 50/5000] english/missing/bm25/deepseek-r1:32b
[campaign 75/5000] english/missing/bm25/deepseek-r1:32b
```

### This is a logging sampling artifact, not skewed data generation

- **The Factorial Structure:** Scenarios are constructed in 25-item blocks:
  $$\text{5 language conditions} \times \text{5 evidence conditions} = \mathbf{25\text{ scenarios per block}}$$
  The 5th language in the loop is `english`, and the 5th evidence condition is `missing`.
- **The Logging Trigger:** The campaign runner prints progress every 25 records:
  ```python
  generated += 1
  if generated % 25 == 0:
      print(f"[campaign {generated}/{total}] {language}/{evidence_condition}/{method}/{model}")
  ```
- Because 25 is an exact multiple of the block size, **every 25th item that triggers the print is always the last scenario of that block** (`english/missing`).
- **The 24 records generated in between** are evenly distributed across `native_bangla`, `translated_bangla`, `code_mixed`, `banglish`, and `correct`, `partially_relevant`, `irrelevant`, `contradictory`.

Inspecting any completed checkpoint verifies perfect balance:
- `native_bangla`: 1,000 records
- `translated_bangla`: 1,000 records
- `code_mixed`: 1,000 records
- `banglish`: 1,000 records
- `english`: 1,000 records

---

## 5. GPU Optimization Guide (NVIDIA GB10 / Host `spark-a405`)

### Architecture Clarification
The system host is named `spark-a405`. Apache Spark is **not** used by this pipeline. The architecture is a native Python harness making local HTTP REST calls to the Ollama server (`http://localhost:11434`), which offloads tensor operations to the NVIDIA GPU via CUDA and `llamacpp`.

### Current Bottlenecks
1. **Serial Execution (`concurrency: 1`):** The default configuration processes requests one by one. While each response takes ~0.47s on `gemma3:4b`, the GPU compute cores remain underutilized between requests.
2. **Context Window Inflation (`262,144 tokens`):** By default, Ollama initializes Qwen/Gemma with their maximum 256K token context window (`-c 262144`), consuming excessive VRAM bandwidth for KV caches when RAG context requires fewer than 4,000 tokens.

---

### Step-by-Step Optimization for 3x–5x Faster Throughput

#### Step 1: Enable Concurrency in Campaign Config

The pipeline in `src/banglarag_eval/pipeline/campaign.py` has built-in `ThreadPoolExecutor` support. Enable it in `configs/campaign_50000_v3_unreviewed.yaml`:

```yaml
generation:
  temperature: 0.0
  max_tokens: 512
  concurrency: 4           # Run 4 requests in parallel (or 8 for smaller 3B/4B models)
  prompt_version: rag_campaign_concise_v3
```

#### Step 2: Start Ollama with Parallel Processing Slots

Restart Ollama with parallel slot allocation enabled:

```bash
OLLAMA_NUM_PARALLEL=4 ollama serve
```

This allocates 4 concurrent execution slots in GPU memory, allowing Ollama to process 4 inference requests in parallel without queueing.

#### Step 3: Restrict Context Window to 4,096 Tokens

In `src/banglarag_eval/pipeline/generator.py`, pass `num_ctx: 4096` in the Ollama request options:

```python
payload = json.dumps({
    "model": model,
    "prompt": prompt,
    "stream": False,
    "think": thinking,
    "options": {
        "temperature": temperature,
        "seed": 42,
        "num_predict": max_tokens,
        "num_ctx": 4096,   # Reduces KV-cache memory overhead by 64x compared to 256K!
    },
}).encode("utf-8")
```

---

### Throughput Comparison

| Configuration | Concurrency | Latency per Response | Time for 5,000 Records |
|---|---|---|---|
| **Default Baseline** | 1 (serial) | ~0.48s | ~40 minutes |
| **Optimized Parallel** | 4 (concurrent) | ~0.15s (effective) | **~12–15 minutes** |
| **High Parallel (3B/4B)** | 8 (concurrent) | ~0.08s (effective) | **~7–9 minutes** |
