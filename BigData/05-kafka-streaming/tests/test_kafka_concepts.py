from __future__ import annotations
from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"01-topic-partitions"));sys.path.insert(0,str(ROOT/"04-idempotent-processing"))
from partition_by_key import partition
from idempotent_consumer import process
class KafkaTests(unittest.TestCase):
 def test_same_key_same_partition(self):self.assertEqual(partition("u1",3),partition("u1",3))
 def test_deduplication(self):self.assertEqual(len(process([{"id":"a"},{"id":"a"}])),1)
