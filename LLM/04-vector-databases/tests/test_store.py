from __future__ import annotations
from pathlib import Path
import sys, unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from vector_store import HashingEmbedder, LocalVectorStore
class StoreTests(unittest.TestCase):
    def setUp(self):
        self.store = LocalVectorStore(HashingEmbedder(64)); self.store.upsert({"id":"a","text":"quantization bellek azaltır","metadata":{"category":"slm"}}); self.store.upsert({"id":"b","text":"rag belge getirir","metadata":{"category":"rag"}})
    def test_upsert_replaces(self):
        self.store.upsert({"id":"a","text":"güncel metin","metadata":{"category":"slm"}}); self.assertEqual(len(self.store.records), 2)
    def test_filter(self): self.assertEqual(self.store.search("belge", filters={"category":"rag"})[0]["id"], "b")
