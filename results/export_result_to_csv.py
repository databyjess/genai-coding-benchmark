"""
Export pilot benchmark results from JSON files to a single CSV file.

Usage:
    python export_results_to_csv.py results/pilot/ pilot_results.csv
"""

import json
import csv
import sys
from pathlib import Path


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def export_to_csv(results_dir: Path, output_csv: Path) -> None:
    rows = []

    for json_file in sorted(results_dir.glob("*.json")):
        data = load_json(json_file)

        model = data["model"]["name"]
        version = data["model"].get("version", "")
        run_date = data["run_metadata"]["run_date"]

        language_scores = data["scores"]["language_scores"]
        overall_score = data["scores"]["overall_score"]

        row = {
            "model": model,
            "version": version,
            "run_date": run_date,
            "python_score": language_scores["python"],
            "sql_score": language_scores["sql"],
            "dax_score": language_scores["dax"],
            "overall_score": overall_score,
        }

        rows.append(row)

    if not rows:
        raise RuntimeError("No result files found")

    fieldnames = rows[0].keys()

    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_results_to_csv.py <results_dir> <output_csv>")
        sys.exit(1)

    results_dir = Path(sys.argv[1])
    output_csv = Path(sys.argv[2])

    export_to_csv(results_dir, output_csv)
    print(f"CSV exported to {output_csv}")
