from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from turkce_slm.prompts import build_user_prompt, normalize_turkish_text


class PromptTests(unittest.TestCase):
    def test_turkish_lowercase(self) -> None:
        self.assertEqual(normalize_turkish_text("İSTANBUL IŞIK"), "istanbul ışık")

    def test_context_is_delimited(self) -> None:
        prompt = build_user_prompt("Özetle", "Birinci cümle.")
        self.assertIn("Bağlam:", prompt); self.assertIn("Yalnızca bağlama", prompt)

    def test_empty_question_rejected(self) -> None:
        with self.assertRaises(ValueError): build_user_prompt("   ")
