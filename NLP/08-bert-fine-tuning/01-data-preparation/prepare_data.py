"""Türkçe yorumları stratified train/validation/test CSV dosyalarına ayırır."""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
import random


def split_rows(rows: list[dict[str, str]], seed: int = 42) -> dict[str, list[dict[str, str]]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows: groups[row["label"]].append(row)
    result = {"train": [], "validation": [], "test": []}; rng = random.Random(seed)
    for label_rows in groups.values():
        rng.shuffle(label_rows); count = len(label_rows)
        validation_size = max(1, round(count * 0.15)); test_size = max(1, round(count * 0.15))
        result["validation"].extend(label_rows[:validation_size]); result["test"].extend(label_rows[validation_size:validation_size + test_size])
        result["train"].extend(label_rows[validation_size + test_size:])
    return result


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]; source = root / "data" / "raw_reviews.csv"; output_dir = root / "data" / "processed"
    with source.open(encoding="utf-8", newline="") as file: rows = list(csv.DictReader(file))
    output_dir.mkdir(exist_ok=True)
    for name, split in split_rows(rows).items():
        with (output_dir / f"{name}.csv").open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["label", "text"]); writer.writeheader(); writer.writerows(split)
        print(f"{name:10}: {len(split)} örnek")
