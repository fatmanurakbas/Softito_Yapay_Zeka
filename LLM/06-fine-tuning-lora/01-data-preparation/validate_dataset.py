"""JSONL talimat verisinin gerekli alanlarını denetler."""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if __name__ == "__main__":
    rows = [json.loads(line) for line in (ROOT / "data" / "train.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    for index, row in enumerate(rows, 1):
        if set(row) != {"instruction", "input", "output"} or not all(isinstance(row[key], str) and row[key].strip() for key in row): raise SystemExit(f"Geçersiz satır: {index}")
    print(f"Veri doğrulandı: {len(rows)} örnek")
