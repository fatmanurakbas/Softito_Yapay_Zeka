"""Canlı karşılaştırma sonuçlarından özet karar tablosu üretir."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from llm_comparison.scoring import summarize_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--input", required=True); args = parser.parse_args()
    rows = json.loads(Path(args.input).read_text(encoding="utf-8")); summary = summarize_results(rows)
    print(f"{'Model':28} {'Örnek':>6} {'Skor':>8} {'Ort. sn':>9} {'JSON':>8}")
    for row in summary: print(f"{row['model']:28} {row['cases']:>6} {row['mean_score']:>8.3f} {row['mean_latency_seconds']:>9.3f} {row['json_valid_rate']:>8.0%}")
