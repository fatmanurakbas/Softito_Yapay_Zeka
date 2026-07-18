from __future__ import annotations
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class ConfigTests(unittest.TestCase):
    def test_quant_options(self):
        cfg=json.loads((ROOT/"configs"/"quant_config.json").read_text()); self.assertIn("base_model",cfg); self.assertIsInstance(cfg["use_nf4"],bool)
