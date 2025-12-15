"""
Score Python tasks based on pytest results and optional quality checks.

Expected input:
- pytest JSON report OR a simple dict with test counts

Output:
- Normalised score (0–100)
"""

from dataclasses import dataclass


@dataclass
class PythonTestResult:
    tests_passed: int
    tests_total: int
    performance_score: float | None = None  # 0–1 scale
    quality_score: float | None = None      # 0–1 scale


def score_python(result: PythonTestResult) -> float:
    if result.tests_total == 0:
        return 0.0

    correctness = (result.tests_passed / result.tests_total) * 70

    if result.performance_score is None:
        performance = 0
        correctness += 20
    else:
        performance = result.performance_score * 20

    quality = (result.quality_score or 0) * 10

    return round(correctness + performance + quality, 2)


if __name__ == "__main__":
    # Example usage
    example = PythonTestResult(
        tests_passed=3,
        tests_total=4,
        performance_score=0.8,
        quality_score=1.0,
    )
    print(score_python(example))
