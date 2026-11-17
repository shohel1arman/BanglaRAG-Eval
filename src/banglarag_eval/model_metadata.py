"""Model provenance metadata used in generated benchmark records."""

from __future__ import annotations

from typing import Any


MODEL_METADATA: dict[str, dict[str, Any]] = {
    "qwen3:4b": {
        "provider": "ollama",
        "family": "Qwen3",
        "parameter_count_billion": 4.0,
        "quantization": "Ollama-managed",
        "license": "Apache-2.0",
        "source": "https://ollama.com/library/qwen3",
    },
    "qwen3:8b": {
        "provider": "ollama",
        "family": "Qwen3",
        "parameter_count_billion": 8.2,
        "quantization": "Ollama-managed",
        "license": "Apache-2.0",
        "source": "https://ollama.com/library/qwen3",
    },
    "gemma3:4b": {
        "provider": "ollama",
        "family": "Gemma 3",
        "parameter_count_billion": 3.9,
        "quantization": "Ollama-managed",
        "license": "Gemma-Terms-of-Use",
        "source": "https://ollama.com/library/gemma3",
    },
    "llama3.2:3b": {
        "provider": "ollama",
        "family": "Llama 3.2",
        "parameter_count_billion": 3.0,
        "quantization": "Ollama-managed",
        "license": "Llama-3.2-Community-License",
        "source": "https://ollama.com/library/llama3.2",
    },
    "phi3.5:3.8b": {
        "provider": "ollama",
        "family": "Phi-3.5 Mini",
        "parameter_count_billion": 3.8,
        "quantization": "Ollama-managed",
        "license": "MIT",
        "source": "https://ollama.com/library/phi3.5",
    },
    "qwen3:32b": {
        "provider": "ollama",
        "family": "Qwen3",
        "parameter_count_billion": 32.8,
        "quantization": "Ollama-managed",
        "license": "Apache-2.0",
        "source": "https://ollama.com/library/qwen3",
    },
    "granite4:32b-a9b-h": {
        "provider": "ollama",
        "family": "IBM Granite 4",
        "parameter_count_billion": 32.2,
        "quantization": "Q4_K_M",
        "license": "Apache-2.0",
        "source": "https://ollama.com/library/granite4:32b-a9b-h",
    },
    "olmo-3.1:32b": {
        "provider": "ollama",
        "family": "OLMo 3.1",
        "parameter_count_billion": 32.2,
        "quantization": "Q4_K_M",
        "license": "Apache-2.0",
        "source": "https://ollama.com/library/olmo-3.1:32b",
    },
    "gemma3:27b": {
        "provider": "ollama",
        "family": "Gemma 3",
        "parameter_count_billion": 27.0,
        "quantization": "Ollama-managed",
        "license": "Gemma-Terms-of-Use",
        "source": "https://ollama.com/library/gemma3",
    },
    "deepseek-r1:32b": {
        "provider": "ollama",
        "family": "DeepSeek-R1 distilled Qwen",
        "parameter_count_billion": 32.0,
        "quantization": "Ollama-managed",
        "license": "MIT",
        "source": "https://ollama.com/library/deepseek-r1",
    },
}


def model_metadata(model: str, configured: dict[str, Any] | None = None) -> dict[str, Any]:
    """Return stable, JSON-compatible provenance for a model tag."""
    details = dict(MODEL_METADATA.get(model, {}))
    if configured:
        details.update(
            {
                key: value
                for key, value in configured.items()
                if key in {"provider", "family", "parameter_count_billion", "quantization", "license", "source"}
            }
        )
        if "parameter_count_billion" not in details and configured.get("parameters"):
            details["parameter_count_billion"] = float(
                str(configured["parameters"]).removesuffix("B")
            )
    details.setdefault("provider", "unknown")
    details.setdefault("family", model.split(":", 1)[0])
    details.setdefault("quantization", "unspecified")
    details["model_name"] = model
    details["ollama_tag"] = (
        model if details["provider"] in {"ollama", "ollama_cloud"} else None
    )
    return details
