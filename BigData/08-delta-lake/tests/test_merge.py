from __future__ import annotations
from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"02-merge-upsert"));from merge_upsert import merge
class MergeTests(unittest.TestCase):
 def test_update_and_insert(self):
  rows={row["id"]:row["amount"] for row in merge([{"id":"a","amount":1}],[{"id":"a","amount":2},{"id":"b","amount":3}])};self.assertEqual(rows,{"a":2,"b":3})
