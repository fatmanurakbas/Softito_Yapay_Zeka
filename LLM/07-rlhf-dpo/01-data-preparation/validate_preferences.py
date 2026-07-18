from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if __name__ == "__main__":
    rows = [json.loads(line) for line in (ROOT / "data" / "preferences.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    for index, row in enumerate(rows, 1):
        if set(row) != {"prompt", "chosen", "rejected"} or not all(isinstance(v, str) and v.strip() for v in row.values()) or row["chosen"] == row["rejected"]: raise SystemExit(f"Geçersiz tercih çifti: {index}")
    print(f"Tercih verisi doğrulandı: {len(rows)} çift")
