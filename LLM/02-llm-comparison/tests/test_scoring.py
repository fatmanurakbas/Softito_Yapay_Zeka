from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from llm_comparison.scoring import score_response, summarize_results


class ScoringTests(unittest.TestCase):
    def test_structured_output_validation(self) -> None:
        self.assertTrue(score_response("structured", '{"label":"positive","reason":"Olumlu."}', [])["json_valid"])
        self.assertFalse(score_response("structured", "geçersiz", [])["json_valid"])

    def test_keyword_coverage(self) -> None:
        self.assertEqual(score_response("qa", "Model bilgi getirir.", ["model", "bilgi"])["automatic_score"], 1.0)

    def test_summary_sorting(self) -> None:
        rows = [{"model": "a", "latency_seconds": 2, "scores": {"automatic_score": 0.5, "json_valid": True}}, {"model": "b", "latency_seconds": 1, "scores": {"automatic_score": 0.8, "json_valid": True}}]
        self.assertEqual(summarize_results(rows)[0]["model"], "b")
