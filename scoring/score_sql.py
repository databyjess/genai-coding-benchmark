"""
Score SQL tasks based on result correctness and query structure review.
"""

from dataclasses import dataclass


@dataclass
class SQLResult:
    result_correct: bool
    structure_score: float  # 0–1 scale


def score_sql(result: SQLResult) -> float:
    correctness = 80 if result.result_correct else 0
    structure = max(0, min(result.structure_score, 1)) * 20
    return round(correctness + structure, 2)


if __name__ == "__main__":
    example = SQLResult(result_correct=True, structure_score=0.5)
    print(score_sql(example))
