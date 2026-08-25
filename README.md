# Benchmarking RAG Faithfulness Evaluation in Low-Resource and Code-Mixed Languages: A Bangla Study

> Research repository — ICLR 2027 target

## Research Objective

We investigate whether existing RAG faithfulness evaluators that perform reasonably well in English remain reliable when transferred to:

- Native Bangla RAG
- Translated Bangla data
- Bangla-English code-mixed RAG
- Controlled retrieval conditions

The project focuses on evaluator reliability, not only model performance. Human annotations will serve as the independent reference standard.

## Research Questions

**RQ1.** How well do existing RAG faithfulness evaluators agree with human judgments on native Bangla RAG?

**RQ2.** How does evaluator reliability change under Bangla-English code-mixing, translated versus native data, and controlled retrieval corruption?

**RQ3.** Which evaluation approach provides the best trade-off between human agreement, robustness, ranking stability, cost, and latency?

## Planned Benchmark Conditions

### Language

1. Native Bangla
2. Translated Bangla
3. Bangla-English code-mixed

### Evidence

1. Correct/relevant
2. Partially relevant
3. Irrelevant
4. Contradictory
5. Missing/no evidence

The benchmark will separate retrieval quality from downstream answer faithfulness.

## Candidate Evaluators

- Human expert annotation
- RAGAS
- Independent LLM-as-a-judge evaluators
- Encoder-based hallucination detectors
- Simple non-neural baselines

The final evaluator set will be determined after the pilot.

## SemFuse

SemFuse may be used as an experimental RAG platform for controlled retrieval and generation experiments.

**Important:** SemFuse's internal grounding/faithfulness mechanism is NOT the benchmark gold standard.

Gold labels must be independently established through human annotation.

## Repository Structure

```text
BanglaRAG-Eval/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── configs/
├── data/
├── docs/
├── experiments/
├── scripts/
├── src/
└── tests/‹
