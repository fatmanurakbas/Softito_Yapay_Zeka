"""Tercih verisinin temel uzunluk ve çeşitlilik denetimi."""
from __future__ import annotations
import argparse, json
from pathlib import Path
if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--input", required=True); args = parser.parse_args()
    rows = [json.loads(line) for line in Path(args.input).read_text(encoding="utf-8").splitlines() if line.strip()]
    better = sum(len(row["chosen"]) != len(row["rejected"]) for row in rows)
    print(f"Tercih çifti: {len(rows)} | Uzunluğu farklı çift: {better / len(rows):.0%}")
    print("Not: uzunluk kalite metriği değildir; insan tercih denetimi gereklidir.")
