from __future__ import annotations
import json
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
class DatasetTests(unittest.TestCase):
    def test_rows_have_schema(self):
        rows = [json.loads(line) for line in (ROOT / "data" / "train.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertTrue(rows); self.assertTrue(all(set(row) == {"instruction", "input", "output"} for row in rows))
