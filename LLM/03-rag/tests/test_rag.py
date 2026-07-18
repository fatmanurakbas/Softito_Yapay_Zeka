from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from rag_core.chunks import build_chunks
from rag_core.prompts import build_rag_messages
from rag_core.retriever import TfidfRetriever


class RagTests(unittest.TestCase):
    def setUp(self) -> None:
        self.docs = [{"id": "a", "title": "A", "text": "quantization bellek tüketimini azaltır"}, {"id": "b", "title": "B", "text": "retrieval ilgili belge getirir"}]

    def test_chunks_keep_document_id(self) -> None:
        self.assertEqual(build_chunks(self.docs, 4, 1)[0]["document_id"], "a")

    def test_retrieval_finds_relevant_document(self) -> None:
        chunks = build_chunks(self.docs, 8, 1); self.assertEqual(TfidfRetriever(chunks).search("bellek quantization", 1)[0]["document_id"], "a")

    def test_prompt_includes_sources(self) -> None:
        message = build_rag_messages("Soru", build_chunks(self.docs, 8, 1))[1]["content"]; self.assertIn("[a-0]", message)
