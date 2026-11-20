# BanglaRAG-Eval: Project Task Tracker & Implementation Status

> [!NOTE]
> **Working Title:** *Benchmarking RAG Faithfulness Evaluation in Low-Resource and Code-Mixed Languages: A Bangla Study*  
> **Target Venue:** ICLR 2027  
> **Active Campaign:** 50,000 records (1,000 base questions $\times$ 5 language conditions $\times$ 5 evidence conditions $\times$ 10 generator models)

---

## 1. High-Level Pipeline & Campaign Architecture

```mermaid
flowchart LR
    A["Raw Data (BanglaQuAD)"] --> B["Question Prep (1,000 Base)"]
    B --> C["Contradiction Synthesis (618 Proposals)"]
    C --> D["Scenario Validation (5,000 Scenarios)"]
    D --> E["Model Generation (50,000 Target)"]
    E --> F["Campaign Finalization"]
    F --> G["Human Annotation & Gates"]
    G --> H["Evaluator Benchmark (6 Evaluators)"]
    H --> I["Statistical Analysis & Paper (ICLR 2027)"]

    style A fill:#e1f5fe,stroke:#0288d1
    style B fill:#e8f5e9,stroke:#388e3c
    style C fill:#e8f5e9,stroke:#388e3c
    style D fill:#e8f5e9,stroke:#388e3c
    style E fill:#fff3e0,stroke:#f57c00
    style F fill:#f5f5f5,stroke:#9e9e9e
    style G fill:#f5f5f5,stroke:#9e9e9e
    style H fill:#f5f5f5,stroke:#9e9e9e
    style I fill:#f5f5f5,stroke:#9e9e9e
```

---

## 2. Active Campaign Status (50,000 Records)

### Phase Breakdown

| Campaign Phase | Scope | Status | Details & Checkpoints |
|---|---|:---:|---|
| **Raw Data Ingestion** | 1,000 QA pairs from BanglaQuAD v1.0 | **Completed** | [BanglaQuADv1.0-train.json](file:///home/izaz/BanglaRAG-Eval/data/raw/BanglaQuADv1.0-train.json) verified (`ec5226...`) |
| **Question Preparation** | 1,000 questions $\times$ 5 language conditions | **Completed** | [campaign_50000_v3_questions.jsonl](file:///home/izaz/BanglaRAG-Eval/data/intermediate/campaign_50000_v3_questions.jsonl) (`b18f20...`) |
| **Contradiction Proposals** | 618 counter-factual candidate replacements | **Completed** | [campaign_50000_v3_contradictions.jsonl](file:///home/izaz/BanglaRAG-Eval/data/intermediate/campaign_50000_v3_contradictions.jsonl) (`5897c7...`) |
| **Scenario Construction Validation** | 5,000 cross-condition scenarios | **Completed** | 100% of scenarios validated with 0 errors |
| **Model Generation (Small / Mid Models)** | 4 models $\times$ 5,000 records | **Completed** | 4/4 completed (`qwen3:4b`, `gemma3:4b`, `llama3.2:3b`, `phi3.5:3.8b`) |
| **Model Generation (8B Model)** | 1 model $\times$ 5,000 records | **Pending / In Progress** | `qwen3:8b` (5,000 records) |
| **Model Generation (Large 27B/32B Models)** | 5 models $\times$ 5,000 records | **Pending** | 36 records completed (`deepseek-r1:32b`); 4 models remaining |
| **Campaign Finalization** | Unified JSONL + Category Manifest | **Pending** | Awaiting completion of generation checkpoints |

---

## 3. Model Generation Matrix (10 Models $\times$ 5,000 Records)

> [!IMPORTANT]
> Total target: **50,000 records**. Current completed: **20,036 / 50,000** (~40.1%).

| Model Tag | Class / Architecture | Target | Completed | Status | Output Checkpoint |
|---|---|:---:|:---:|:---:|---|
| `qwen3:4b` | Dense Small (4.0B) | 5,000 | 5,000 | **Done** | [campaign_qwen3_4b_working.jsonl](file:///home/izaz/BanglaRAG-Eval/checkpoints/campaign_qwen3_4b_working.jsonl) |
| `gemma3:4b` | Dense Small (3.9B) | 5,000 | 5,000 | **Done** | [campaign_gemma3_4b_working.jsonl](file:///home/izaz/BanglaRAG-Eval/checkpoints/campaign_gemma3_4b_working.jsonl) |
| `llama3.2:3b` | Dense Small (3.2B) | 5,000 | 5,000 | **Done** | [campaign_llama3_2_3b_working.jsonl](file:///home/izaz/BanglaRAG-Eval/checkpoints/campaign_llama3_2_3b_working.jsonl) |
| `phi3.5:3.8b` | Dense Small (3.8B) | 5,000 | 5,000 | **Done** | [campaign_phi3_5_3_8b_working.jsonl](file:///home/izaz/BanglaRAG-Eval/checkpoints/campaign_phi3_5_3_8b_working.jsonl) |
| `qwen3:8b` | Dense Mid (8.2B) | 5,000 | 0 | **Pending** | `checkpoints/campaign_qwen3_8b_working.jsonl` |
| `deepseek-r1:32b` | Reasoning Large (32B) | 5,000 | 36 | **Paused** | [campaign_deepseek-r1_32b_working.jsonl](file:///home/izaz/BanglaRAG-Eval/checkpoints/campaign_deepseek-r1_32b_working.jsonl) |
| `qwen3:32b` | Dense Large (32.5B) | 5,000 | 0 | **Pending** | `checkpoints/campaign_qwen3_32b_working.jsonl` |
| `granite4:32b-a9b-h` | MoE Large (32B-A9B) | 5,000 | 0 | **Pending** | `checkpoints/campaign_granite4_32b-a9b-h_working.jsonl` |
| `gemma3:27b` | Dense Large (27.2B) | 5,000 | 0 | **Pending** | `checkpoints/campaign_gemma3_27b_working.jsonl` |
| `olmo-3.1:32b` | Dense Large (32.1B) | 5,000 | 0 | **Pending** | `checkpoints/campaign_olmo-3.1_32b_working.jsonl` |

---

## 4. Master Task Tracker (Milestones M1 – M3)

### Milestone 1: Foundations & Architecture
- [x] Canonical Record Schema ([record.schema.json](file:///home/izaz/BanglaRAG-Eval/configs/record.schema.json)) Draft 2020-12
- [x] Schema Validation Module ([schema.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/schema.py)) enforcing Rules R1–R10
- [x] Deterministic 10-example Synthetic Fixture ([synthetic_fixture_v0.jsonl](file:///home/izaz/BanglaRAG-Eval/data/fixtures/synthetic_fixture_v0.jsonl))
- [x] 100% test coverage on synthetic fixtures and schema constraints

### Milestone 2: Core Pipeline & Evaluator Infrastructure
- [x] **Issue #3:** Source Document Interface ([sources.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/pipeline/sources.py))
- [x] **Issue #4:** Question Generation & Translation ([campaign.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/pipeline/campaign.py))
  - [x] BanglaT5 bidirectional NMT interface
  - [x] Ollama-based transformation fallback
  - [x] Code-mixing and Banglish transliteration rules
  - [x] Programmatic answer leakage check (`_answer_leaks`)
- [x] **Issue #5:** Retrieval Pipeline ([retrieval/](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/retrieval/))
  - [x] Lexical BM25 with Unicode Bangla/English tokenization
  - [x] Deduplication and passage rank integrity
- [x] **Issue #6:** Generation Pipeline ([generator.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/pipeline/generator.py))
  - [x] Local Ollama REST API integration
  - [x] `<think>` tag stripping for reasoning models
  - [x] `max_tokens` reasoning diagnosis and optimization guide ([GENERATION_OPTIMIZATION_GUIDE.md](file:///home/izaz/BanglaRAG-Eval/docs/GENERATION_OPTIMIZATION_GUIDE.md))
- [x] **Issue #7:** Controlled Evidence Construction ([evidence.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/pipeline/evidence.py))
  - [x] 5 evidence conditions: `correct`, `partially_relevant`, `irrelevant`, `contradictory`, `missing`
  - [x] Corruption metadata tracking
- [x] **Issue #8:** Real Pilot Dataset (500 records in [pilot_stage1_real.jsonl](file:///home/izaz/BanglaRAG-Eval/data/pilot_stage1_real.jsonl))
- [ ] **Issue #9:** Human Annotation & Adjudication Protocol
  - [x] Annotation Web UI ([run_annotation_server.py](file:///home/izaz/BanglaRAG-Eval/scripts/run_annotation_server.py))
  - [x] Annotation working copy generator ([setup_annotation.py](file:///home/izaz/BanglaRAG-Eval/scripts/setup_annotation.py))
  - [ ] Execute 2-rater blind annotation on pilot sample
  - [ ] Complete third-rater adjudication on disagreements
- [x] **Issue #10:** Stage-1 Gate Measurement Module ([gates.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/gates.py))
  - [x] Condition integrity gate ($\ge 90\%$)
  - [x] Pipeline integrity gate (100% schema valid)
  - [x] Evaluator harness gate ($\ge 95\%$ valid outputs)
  - [ ] Inter-annotator agreement gate (Cohen's $\kappa \ge 0.60$ — pending human labels)
  - [ ] Taxonomy adequacy gate ($\le 5\%$ NO-FIT — pending human labels)
- [x] **Issue #11:** Evaluator Suite ([evaluators/](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/evaluators/))
  - [x] `lexical_baseline` (lexical overlap + negation penalty)
  - [x] `exact_match` (token TF precision/recall)
  - [x] `answer_relevance` (question type alignment + content token recall)
  - [x] `nli_entailment` (zero-shot NLI via Ollama)
  - [x] `ragas_faithfulness` (local claim extraction + NLI verification)
  - [x] LLM-as-a-judge adapter (Qwen/OpenAI/Anthropic)
- [x] **Issue #12:** Metrics Engine ([metrics.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/analysis/metrics.py))
- [x] **Issue #13:** Statistical Analysis Module ([statistics.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/analysis/statistics.py))
  - [x] Cluster bootstrap resampling (clustered by `split_group_id`)
  - [x] McNemar test for paired evaluator discordance
- [x] **Issue #14:** Ranking Stability Module ([ranking.py](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/analysis/ranking.py))
  - [x] Spearman $\rho$ and Kendall $\tau$ with tie handling
- [x] **Issue #15:** SemFuse RAGBackend Integration ([rag_backend/](file:///home/izaz/BanglaRAG-Eval/src/banglarag_eval/rag_backend/))

---

### Milestone 3: Scale-Up, Full Campaign & ICLR 2027 Publication
- [ ] **Issue #16:** Scale to Full 50,000-Record Pre-Annotation Campaign
  - [x] Question preparation & SHA-256 lock ([campaign_50000_v3_unreviewed.yaml](file:///home/izaz/BanglaRAG-Eval/configs/campaign_50000_v3_unreviewed.yaml))
  - [x] Contradiction proposals generated (617 auto + 2 curated)
  - [x] Complete 5,000 records for `qwen3:4b`
  - [x] Complete 5,000 records for `gemma3:4b`
  - [ ] Complete remaining small/mid models (`llama3.2:3b`, `phi3.5:3.8b`, `qwen3:8b`)
  - [ ] Complete 32B/27B models (`deepseek-r1:32b`, `qwen3:32b`, `granite4:32b-a9b-h`, `gemma3:27b`, `olmo-3.1:32b`)
  - [ ] Finalize combined dataset via `scripts/run_campaign.py finalize`
- [ ] **Issue #17:** Meta-Evaluation Benchmarking & Paper Writing
  - [ ] Run all 6 automated evaluators across all 50,000 generated records
  - [ ] Cross-lingual performance comparison (English vs. Native vs. Code-Mixed vs. Banglish)
  - [ ] Controlled evidence corruption analysis (detecting hallucinations under contradictory/partial/irrelevant evidence)
  - [ ] Ranking stability across evaluator families
  - [ ] ICLR 2027 Full Paper submission

---

## 5. Immediate Next Actions

1. **Update `max_tokens: 512` in Config:** Apply the tested DeepSeek-R1 fix to [configs/campaign_50000_v3_unreviewed.yaml](file:///home/izaz/BanglaRAG-Eval/configs/campaign_50000_v3_unreviewed.yaml#L150).
2. **Resume DeepSeek-R1 32B Generation:** Resume `checkpoints/campaign_deepseek-r1_32b_working.jsonl` from record 37 to 5,000.
3. **Run Remaining Small Models:** Generate `llama3.2:3b`, `phi3.5:3.8b`, and `qwen3:8b` (using parallel batching for fast ~15-minute runs).
4. **Run Remaining 32B Family:** Generate `qwen3:32b`, `granite4:32b-a9b-h`, `gemma3:27b`, and `olmo-3.1:32b`.
5. **Finalize Checkpoints:** Consolidate working files into canonical `data/campaign_*.jsonl` datasets.
