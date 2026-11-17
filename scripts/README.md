# Maintained scripts

The repository keeps one canonical entry point for each distinct workflow.
Version-specific shell launchers and one-time migration/audit utilities are
not maintained.

- `run_pipeline.py` — run the single-model pilot pipeline. Select the model
  with `--model MODEL` or `OLLAMA_MODEL`.
- `run_campaign.py` — run the versioned campaign through `prepare`, `repair`,
  `propose-contradictions`, `review`, `generate`, `finalize`, or `all`.
  Select one model with `--model MODEL`, several with `--models MODEL...`, or
  omit the option to run every configured model.
- `run_evaluators.py` — run automatic evaluators and compute metrics.
- `filter_dataset.py` — create a model-specific JSONL subset from a completed
  multi-model dataset.
- `setup_annotation.py` — create a human-annotation working copy.
- `run_annotation_server.py` — start the local Flask annotation UI.
- `build_synthetic_fixture.py` — regenerate the deterministic test fixture;
  tests enforce builder/output synchronization.

For the complete campaign workflow, use the canonical Python command:

```bash
.venv/bin/python scripts/run_campaign.py all
```

Run one model only:

```bash
.venv/bin/python scripts/run_campaign.py generate \
  --model qwen3:4b \
  --working checkpoints/campaign_qwen3_4b_working.jsonl \
  --output data/campaign_qwen3_4b.jsonl
```

Filter a completed dataset by model:

```bash
.venv/bin/python scripts/filter_dataset.py \
  --dataset data/campaign_45000_v3_unreviewed.jsonl \
  --model qwen3:4b \
  --output data/campaign_qwen3_4b.jsonl
```
