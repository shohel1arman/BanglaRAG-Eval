from __future__ import annotations

from banglarag_eval.model_metadata import model_metadata
from banglarag_eval.pipeline.campaign import load_campaign_config


def test_small_model_metadata_is_structured() -> None:
    details = model_metadata("qwen3:4b")

    assert details["model_name"] == "qwen3:4b"
    assert details["family"] == "Qwen3"
    assert details["parameter_count_billion"] == 4.0
    assert details["ollama_tag"] == "qwen3:4b"


def test_campaign_model_selection_recalculates_target() -> None:
    config = load_campaign_config(
        "configs/campaign_10000_v3_unreviewed.yaml",
        generator_models=["qwen3:4b", "llama3.2:3b"],
    )

    assert config["generator_models"] == ["qwen3:4b", "llama3.2:3b"]
    assert config["target_records"] == 10_000
