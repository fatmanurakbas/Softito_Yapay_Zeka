from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from prompt_lab.templates import PromptTemplateStore


class TemplateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = PromptTemplateStore(ROOT / "prompts" / "templates.json")

    def test_render_summary(self) -> None:
        messages = self.store.render("summary", text="Örnek metin")
        self.assertEqual(messages[0]["role"], "system"); self.assertIn("Örnek metin", messages[1]["content"])

    def test_unknown_task(self) -> None:
        with self.assertRaises(ValueError): self.store.render("bilinmeyen", text="x")
