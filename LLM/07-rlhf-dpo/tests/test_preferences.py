from __future__ import annotations
import json
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
class PreferenceTests(unittest.TestCase):
    def test_schema(self):
        rows = [json.loads(line) for line in (ROOT / "data" / "preferences.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertTrue(all(set(row) == {"prompt", "chosen", "rejected"} and row["chosen"] != row["rejected"] for row in rows))
