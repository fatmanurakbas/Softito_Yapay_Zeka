"""Harici kütüphane olmadan ikili sınıflandırma metrikleri hesaplar."""
from __future__ import annotations

import argparse
import csv


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--predictions", required=True); args = parser.parse_args()
    with open(args.predictions, encoding="utf-8", newline="") as file: rows = list(csv.DictReader(file))
    expected = [int(row["expected"]) for row in rows]; predicted = [int(row["predicted"]) for row in rows]
    f1_scores = []
    for label in (0, 1):
        tp = sum(p == label and e == label for e, p in zip(expected, predicted)); fp = sum(p == label and e != label for e, p in zip(expected, predicted)); fn = sum(p != label and e == label for e, p in zip(expected, predicted))
        precision, recall = tp / (tp + fp + 1e-9), tp / (tp + fn + 1e-9); f1 = 2 * precision * recall / (precision + recall + 1e-9); f1_scores.append(f1)
        print(f"Sınıf {label}: precision={precision:.3f}, recall={recall:.3f}, f1={f1:.3f}")
    print(f"accuracy={sum(e == p for e, p in zip(expected, predicted)) / len(rows):.3f}, macro_f1={sum(f1_scores) / 2:.3f}")
