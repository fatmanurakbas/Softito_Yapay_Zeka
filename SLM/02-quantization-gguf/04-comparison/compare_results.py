"""GGUF benchmark CSV sonucunu model adına göre özetler."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--input", required=True); args = parser.parse_args()
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    with open(args.input, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file): groups[row["model"]].append(row)
    print(f"{'Model':40} {'Çalıştırma':>10} {'Ort. sn':>10} {'Ort. tok/sn':>12}")
    for model, rows in sorted(groups.items(), key=lambda item: -sum(float(row["approx_tokens_per_second"]) for row in item[1]) / len(item[1])):
        seconds = sum(float(row["wall_seconds"]) for row in rows) / len(rows); speed = sum(float(row["approx_tokens_per_second"]) for row in rows) / len(rows)
        print(f"{model:40} {len(rows):>10} {seconds:>10.2f} {speed:>12.2f}")
