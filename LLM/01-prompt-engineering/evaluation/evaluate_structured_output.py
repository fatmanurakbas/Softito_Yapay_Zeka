"""Kayıtlı prompt çıktılarını JSON şemasına uygunluk açısından ölçer."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from prompt_lab.schemas import validate_output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--input", required=True); args = parser.parse_args()
    rows = json.loads(Path(args.input).read_text(encoding="utf-8")); valid = 0
    for index, row in enumerate(rows, start=1):
        passed, message = validate_output(row["task"], row["output"]); valid += passed
        print(f"{index}. {row['task']}: {'OK' if passed else 'HATA'} — {message}")
    print(f"Şema uygunluğu: {valid / len(rows):.0%} ({len(rows)} örnek)")
