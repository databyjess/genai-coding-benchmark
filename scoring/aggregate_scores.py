"""
Aggregate task-level scores into language-level and overall model scores.
"""

from dataclasses import dataclass


LANGUAGE_WEIGHTS = {
    "python": 0.4,
    "sql": 0.4,
    "dax": 0.2,
}


@dataclass
class LanguageScores:
    python: list[float]
    sql: list[float]
    dax: list[float]


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 2) if values else 0.0


def aggregate(scores: LanguageScores) -> dict:
    python_score = mean(scores.python)
    sql_score = mean(scores.sql)
    dax_score = mean(scores.dax)

    overall = (
        python_score * LANGUAGE_WEIGHTS["python"]
        + sql_score * LANGUAGE_WEIGHTS["sql"]
        + dax_score * LANGUAGE_WEIGHTS["dax"]
    )

    return {
        "python": python_score,
        "sql": sql_score,
        "dax": dax_score,
        "overall": round(overall, 2),
    }


if __name__ == "__main__":
    example = LanguageScores(
        python=[85, 90],
        sql=[70],
        dax=[60],
    )
    print(aggregate(example))
