# Research Protocol

## Working Title

**Benchmarking RAG Faithfulness Evaluation in Low-Resource and Code-Mixed Languages: A Bangla Study**

## Target Venue

ICLR 2027 — preliminary target.

The exact title and contribution will be finalized after the pilot experiments.

## 1. Core Research Problem

Do RAG faithfulness evaluators that perform reasonably well in English remain reliable when transferred to native Bangla and Bangla-English code-mixed RAG?

The project studies the reliability of the evaluation methods themselves, rather than simply ranking RAG systems.

## 2. Preliminary Research Questions

### RQ1

How well do existing RAG faithfulness evaluators agree with human judgments on native Bangla RAG?

### RQ2

How does evaluator reliability change under:

- Bangla-English code-mixing;
- translated versus native data;
- controlled retrieval corruption?

### RQ3

Which evaluation approach provides the best trade-off between:

- human agreement;
- robustness;
- ranking stability;
- cost;
- latency?

## 3. Preliminary Hypotheses

The following are hypotheses only and must not be treated as expected results:

- Existing automatic evaluators may show reduced agreement with human judgments in Bangla.
- Code-mixed inputs may expose additional evaluator weaknesses.
- Different evaluator families may rank RAG systems differently.
- Lower-cost encoder-based methods may provide competitive performance under some conditions.

All hypotheses will be tested empirically.

## 4. Benchmark Language Conditions

### A. Native Bangla

Native Bangla questions, evidence, and responses.

### B. Translated Bangla

A controlled Bangla adaptation of an established English RAG hallucination resource where licensing and methodology permit.

### C. Bangla-English Code-Mixed

Bangla-English mixed-language queries, contexts, and/or responses.

## 5. Evidence Conditions

The benchmark should investigate controlled evidence conditions:

1. Correct/relevant evidence
2. Partially relevant evidence
3. Irrelevant evidence
4. Contradictory evidence
5. Missing/no evidence

These conditions allow retrieval quality and answer faithfulness to be analyzed separately.

## 6. Human Annotation

Human annotation is the independent reference standard.

The annotation protocol must define:

- what constitutes a faithful claim;
- what constitutes an unsupported claim;
- what constitutes contradiction;
- span-level hallucination;
- response-level faithfulness;
- treatment of ambiguous evidence;
- adjudication procedure.

Inter-annotator agreement must be measured before scaling the benchmark.

## 7. Automatic Evaluators

Candidate evaluators include:

- RAGAS;
- independent LLM judges;
- encoder-based hallucination detectors;
- simple lexical/non-neural baselines.

The final evaluator suite will be determined after the pilot.

## 8. SemFuse

SemFuse may be used to construct controlled RAG experiments.

SemFuse's internal grounding or faithfulness score must **not** be treated as the benchmark gold label.

The benchmark evaluates automatic evaluators against independently produced human annotations.

## 9. Pilot Study

Initial target:

**300–500 carefully selected examples.**

The pilot must answer:

1. Can annotators agree reliably?
2. Are the annotation definitions sufficiently clear?
3. Do automatic evaluators disagree with humans?
4. Does Bangla expose evaluator weaknesses?
5. Does code-mixing introduce additional evaluator errors?
6. Are the evidence corruption conditions useful?
7. Is the benchmark scalable?

## 10. Evaluation Metrics

Candidate metrics include:

### Classification

- Precision
- Recall
- F1
- AUROC
- Balanced Accuracy

### Agreement

- Cohen's kappa where applicable
- Krippendorff's alpha where appropriate
- Human–automatic evaluator agreement

### Correlation

- Spearman correlation
- Pearson correlation where assumptions are appropriate

### Ranking

- Rank correlation
- Pairwise ranking agreement
- Ranking stability across evaluators

### Efficiency

- Cost per 1,000 examples
- Latency
- Throughput
- GPU/CPU requirements

Statistical confidence intervals and appropriate paired tests will be used.

## 11. Reproducibility

Every experiment must record:

- dataset version;
- Git commit;
- configuration;
- model and version;
- prompts;
- retrieval configuration;
- random seed where applicable;
- evaluation implementation/version;
- hardware;
- runtime;
- cost.

## 12. Research Integrity

The project must avoid:

- evaluator circularity;
- leakage between training and evaluation;
- post-hoc hypothesis changes;
- undocumented prompt changes;
- cherry-picked examples;
- unsupported novelty claims.

All major methodological decisions should be documented before the main experiments.

## 13. Decision Gate

The full benchmark should only be constructed after the pilot demonstrates:

- acceptable annotation agreement;
- meaningful evaluator disagreement or transfer effects;
- a stable and defensible annotation taxonomy;
- feasibility of the proposed evaluation protocol.

The final paper contribution will be determined from the empirical findings.
