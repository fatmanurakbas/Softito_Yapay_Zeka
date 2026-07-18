from __future__ import annotations
from pathlib import Path
import sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"03-batch-inference"));from batch_inference import score
class BatchTests(unittest.TestCase):
 def test_score_range(self):self.assertTrue(0<=score({"events":100,"amount":100})<=1)
