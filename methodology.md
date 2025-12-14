# Methodology

This document describes the experimental methodology used in the **GenAI Coding Benchmark**. The aim is to ensure that results are **fair, reproducible, transparent, and practically meaningful**.

---

## 1. Study design

This benchmark follows a **controlled, task-based comparative design**.

* Each model is evaluated on the *same fixed set of tasks*
* Tasks are executed independently and scored using identical criteria
* Model identities are hidden during human review where applicable
* Results are aggregated per language and per model

The study is designed to prioritise **internal validity** over breadth, favouring reliable comparisons over exhaustive feature coverage.

---

## 2. Models evaluated

The benchmark focuses on **browser-based generative AI systems**, accessed through their public chat interfaces.

Key characteristics:

* No IDE context or file-system access
* No agent-based or autonomous execution
* Prompts entered manually or via scripted copy-paste

Model names, versions, and execution dates are recorded for each run. Results are **time-bound** and reflect model behaviour at the time of evaluation.

---

## 3. Programming languages and task categories

### Python

Python tasks represent **general-purpose data-related programming** and include:

* Data loading and transformation
* Algorithmic problem solving
* Validation and error handling
* Performance-conscious implementations

All Python tasks target **Python 3.11**.

### SQL

SQL tasks represent **analytical and reporting workloads** and include:

* Aggregations and joins
* Window functions
* Time-based analysis
* Performance-aware query design

Queries are required to be **ANSI SQL**, with Postgres compatibility.

### DAX

DAX tasks represent **semantic-layer and BI logic** and include:

* Measure creation
* Filter and row context handling
* Time intelligence
* Safe aggregation and division

Due to limited automation support, DAX tasks are evaluated via structured human review and reported separately.

---

## 4. Task selection

Tasks are designed to be:

* Representative of real-world enterprise workloads
* Solvable without external documentation
* Independent of proprietary schemas or business logic

Each task is defined as a JSON file containing:

* Task description and constraints
* Expected inputs and outputs
* Evaluation requirements

Tasks are categorised by language and difficulty (easy / medium / hard).

---

## 5. Prompting strategy

To ensure fairness:

* A **single prompt template per language** is used
* Prompts specify explicit constraints (language version, output format)
* No iterative refinement or follow-up questions are allowed

Each task is executed **multiple times per model** to assess robustness and variance.

---

## 6. Execution procedure

For each task and model:

1. The prompt is submitted via the browser interface
2. The full response is captured verbatim
3. Metadata is recorded (model, version, timestamp, latency)
4. Outputs are stored unmodified for evaluation

All executions are performed within a short, predefined time window to minimise model drift.

---

## 7. Evaluation criteria

### 7.1 Python and SQL (automated evaluation)

Python and SQL solutions are evaluated using automated tests and static analysis.

Primary criteria:

* Functional correctness (unit tests)
* Performance (task-dependent benchmarks)
* Code quality and readability
* Basic safety and correctness patterns

Automated evaluation ensures objectivity and repeatability.

### 7.2 DAX (expert review)

DAX solutions are evaluated using a structured checklist by reviewers with DAX experience.

Evaluation focuses on:

* Correct use of CALCULATE and FILTER
* Proper handling of filter and row context
* Correct time intelligence logic
* Safe division and BLANK handling

Each criterion is scored as pass, partial, or fail.

---

## 8. Scoring and aggregation

Scores are computed per task and aggregated as follows:

* Task-level scores are normalised to a 0–100 scale
* Scores are aggregated per language per model
* Python and SQL form the **primary composite score**
* DAX results are reported separately as an enterprise-relevance signal

This avoids over-weighting niche language performance while preserving insight.

---

## 9. Statistical considerations

Where sufficient data is available:

* Non-parametric tests are used to compare models across tasks
* Effect sizes are preferred over raw score differences
* Variance across runs is reported to assess stability

The emphasis is on **practical significance**, not only statistical significance.

---

## 10. Reproducibility and transparency

This benchmark emphasises reproducibility:

* Prompts, datasets, and scoring logic are version-controlled
* Raw outputs are preserved (subject to repository constraints)
* Execution dates and model versions are logged

Any deviations from this methodology are documented explicitly.

---

## 11. Limitations

This study intentionally does not measure:

* IDE-level productivity gains
* Developer experience or ergonomics
* Long-running agent behaviour
* Proprietary enterprise integrations

Results should therefore be interpreted within the defined scope.

---

## 12. Ethical and legal considerations

* Generated code is reviewed for obvious unsafe patterns
* No proprietary or confidential data is used
* The benchmark does not claim ownership over model outputs

Users are responsible for verifying licence compatibility before using generated code in production.

---

## 13. Change log

Significant methodological changes will be recorded here to preserve comparability over time.
