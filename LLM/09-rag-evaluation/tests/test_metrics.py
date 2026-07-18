from __future__ import annotations
from pathlib import Path
import sys,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from rag_eval.metrics import answer_metrics,retrieval_metrics
class MetricTests(unittest.TestCase):
    def test_recall(self): self.assertEqual(retrieval_metrics(["a"],["b","a"],2)["recall_at_k"],1.0)
    def test_faithfulness(self): self.assertEqual(answer_metrics("x",[],["a"],["a"])["citation_faithfulness"],1.0)
