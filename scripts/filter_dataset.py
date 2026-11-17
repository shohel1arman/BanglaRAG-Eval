#!/usr/bin/env python3
"""Select records for one or more generator models from a JSONL dataset."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", required=True, help="Input JSONL dataset")
    parser.add_argument("--model", "--models", dest="models", nargs="+", required=True)
    parser.add_argument("--output", required=True, help="Filtered JSONL output")
    args = parser.parse_args()
    selected = set(args.models)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    counts: Counter[str] = Counter()
    written = 0
    with open(args.dataset, encoding="utf-8") as source, open(
        output, "w", encoding="utf-8"
    ) as target:
        for line in source:
            if not line.strip():
                continue
            record = json.loads(line)
            model = record.get("generator_model")
            if model in selected:
                target.write(json.dumps(record, ensure_ascii=False) + "\n")
                counts[model] += 1
                written += 1
    if not written:
        raise SystemExit(f"No records matched {sorted(selected)} in {args.dataset}")
    print(f"Wrote {written} records to {output}")
    print(f"Model counts: {dict(sorted(counts.items()))}")


if __name__ == "__main__":
    main()
