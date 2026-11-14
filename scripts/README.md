# Maintained scripts

The repository keeps one canonical entry point for each distinct workflow.
Version-specific shell launchers and one-time migration/audit utilities are
not maintained.

- `run_pipeline.py` — run the single-model pilot pipeline. Select the model
  with `--model MODEL` or `OLLAMA_MODEL`.
- `run_campaign.py` — run the versioned campaign through `prepare`, `repair`,
  `propose-contradictions`, `review`, `generate`, `finalize`, or `all`.
- `run_evaluators.py` — run automatic evaluators and compute metrics.
- `setup_annotation.py` — create a human-annotation working copy.
- `run_annotation_server.py` — start the local Flask annotation UI.
- `build_synthetic_fixture.py` — regenerate the deterministic test fixture;
  tests enforce builder/output synchronization.

For the complete campaign workflow, use the canonical Python command:

```bash
.venv/bin/python scripts/run_campaign.py all
```
