from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from prompt_lab.schemas import validate_output


class SchemaTests(unittest.TestCase):
    def test_valid_sentiment(self) -> None:
        self.assertTrue(validate_output("sentiment", '{"label":"positive","reason":"Olumlu."}')[0])

    def test_invalid_sentiment_label(self) -> None:
        self.assertFalse(validate_output("sentiment", '{"label":"mixed","reason":"Belirsiz."}')[0])

    def test_invalid_json(self) -> None:
        self.assertFalse(validate_output("extraction", "json değil")[0])
