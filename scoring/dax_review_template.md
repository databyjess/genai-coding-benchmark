# DAX Review Template

This template is used for **structured human evaluation** of DAX solutions in the GenAI Coding Benchmark.

It ensures consistency, transparency, and comparability across reviewers and models.

---

## 1. Review metadata

* **Task ID:**
* **Model name:**
* **Model version (if known):**
* **Review date:**
* **Reviewer:**

---

## 2. DAX solution under review

Paste the generated DAX measure below:

```DAX
-- Paste model-generated DAX here
```

---

## 3. Evaluation checklist

Each criterion should be marked as:

* **Pass** — fully correct
* **Partial** — mostly correct, minor issues
* **Fail** — incorrect or fundamentally flawed

### 3.1 Correct use of CALCULATE

* Does the solution correctly use `CALCULATE` to modify filter context?

**Score:** ☐ Pass ☐ Partial ☐ Fail

---

### 3.2 Filter application on dimension table

* Is the filter on the dimension table (e.g. `Products[Category]`) applied correctly?
* Is it resilient to slicers and report filters?

**Score:** ☐ Pass ☐ Partial ☐ Fail

---

### 3.3 Respect for existing filter context

* Does the measure respect existing filters (especially date filters)?
* Does it avoid unintentionally removing context with `ALL` or similar functions?

**Score:** ☐ Pass ☐ Partial ☐ Fail

---

### 3.4 Conditional logic and BLANK handling

* Is conditional logic implemented correctly?
* Is `BLANK()` returned where required instead of `0`?

**Score:** ☐ Pass ☐ Partial ☐ Fail

---

### 3.5 Idiomatic and maintainable DAX

* Is the measure readable and idiomatic?
* Are unnecessary variables or overly complex constructs avoided?

**Score:** ☐ Pass ☐ Partial ☐ Fail

---

## 4. Overall assessment

### Overall correctness

☐ Fully correct
☐ Mostly correct
☐ Incorrect

---

### Reviewer notes

Provide brief justification, highlighting strengths and issues:

```
```

---

## 5. Numerical scoring (for aggregation)

Convert checklist results into a numeric score:

* Pass = 2 points
* Partial = 1 point
* Fail = 0 points

**Maximum score:** 10 points

**Total score:** ___ / 10

---

## 6. Final verdict

☐ Acceptable solution for production-like use
☐ Acceptable with reservations
☐ Not acceptable

---

## 7. Review consistency check (optional)

If multiple reviewers assess the same solution:

* Record score variance
* Discuss discrepancies
* Agree on a final consolidated score

This step is recommended for pilot tasks to ensure scoring alignment.
