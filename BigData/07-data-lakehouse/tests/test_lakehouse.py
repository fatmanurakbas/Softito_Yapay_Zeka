from __future__ import annotations
from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"01-medallion-layers"));sys.path.insert(0,str(ROOT/"02-schema-evolution"));from medallion_pipeline import gold;from schema_evolution import compatible
class LakehouseTests(unittest.TestCase):
 def test_gold_aggregation(self):self.assertEqual(gold([{"amount":2.0},{"amount":3.0}])["revenue"],5.0)
 def test_additive_schema(self):self.assertTrue(compatible({"a"},{"a","b"}))
