from __future__ import annotations
import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"02-partition-planning"))
from partition_planner import plan
class PartitionTests(unittest.TestCase):
 def test_preserves_total_size(self):self.assertEqual(sum(plan([100,200,300],256)),600)
