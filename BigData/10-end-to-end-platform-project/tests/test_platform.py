from __future__ import annotations
from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"01-ingestion"));sys.path.insert(0,str(ROOT/"02-lakehouse-transform"));from ingest_events import deduplicate;from transform_events import transform
class PlatformTests(unittest.TestCase):
 def test_deduplicate(self):self.assertEqual(len(deduplicate([{"event_id":"a"},{"event_id":"a"}])),1)
 def test_gold_revenue(self):self.assertEqual(transform([{"event_id":"a","event_type":"purchase","amount":4}])[1]["revenue"],4)
