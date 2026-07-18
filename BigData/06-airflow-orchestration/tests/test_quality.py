from __future__ import annotations
from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"04-data-quality-gate"));from data_quality_gate import validate
class QualityTests(unittest.TestCase):
 def test_valid_rows(self):self.assertEqual(validate([{"id":"a","amount":1}]),[])
 def test_duplicate_ids(self):self.assertIn("Tekrarlanan id bulundu.",validate([{"id":"a","amount":1},{"id":"a","amount":2}]))
