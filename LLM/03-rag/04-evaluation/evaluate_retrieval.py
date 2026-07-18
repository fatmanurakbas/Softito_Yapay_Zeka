"""Bilinen doğru kaynaklara göre retrieval recall@k hesaplar."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from rag_core.chunks import build_chunks
from rag_core.retriever import TfidfRetriever


if __name__ == "__main__":
    config = json.loads((ROOT / "configs" / "app_config.json").read_text(encoding="utf-8")); docs = json.loads((ROOT / "data" / "documents.json").read_text(encoding="utf-8")); retriever = TfidfRetriever(build_chunks(docs, config["chunk_size"], config["chunk_overlap"]))
    cases = [("Quantization ne sağlar?", "quantization"), ("Chunk overlap neden kullanılır?", "chunking"), ("Recall@k neyi ölçer?", "evaluation")]; hits = 0
    for query, expected in cases:
        results = retriever.search(query, config["top_k"]); found = any(item["document_id"] == expected for item in results); hits += found; print(f"{'OK' if found else 'HATA'} | {query} | {[item['document_id'] for item in results]}")
    print(f"Recall@{config['top_k']}: {hits / len(cases):.0%}")
