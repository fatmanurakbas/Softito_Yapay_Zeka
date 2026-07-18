from __future__ import annotations
from pathlib import Path
import sys, unittest
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "03-rag")); sys.path.insert(0, str(ROOT / "src"))
class StructureTests(unittest.TestCase):
    def test_config_exists(self): self.assertTrue((ROOT / "configs" / "app_config.json").is_file())
    def test_documents_exist(self): self.assertTrue((ROOT / "data" / "documents.json").is_file())
