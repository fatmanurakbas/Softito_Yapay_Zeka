from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from turkce_slm.config import AppConfig


class ConfigTests(unittest.TestCase):
    def test_valid_config(self) -> None:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as file:
            file.write('{"model":"yerel-model","temperature":0.3,"num_ctx":1024,"max_output_tokens":64}')
            path = file.name
        self.assertEqual(AppConfig.from_file(path).model, "yerel-model")
        Path(path).unlink()

    def test_invalid_temperature(self) -> None:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as file:
            file.write('{"model":"yerel-model","temperature":3}')
            path = file.name
        with self.assertRaises(ValueError): AppConfig.from_file(path)
        Path(path).unlink()
