"""RAG bilgi tabanında sorgu araması."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from rag_core.chunks import build_chunks
from rag_core.retriever import TfidfRetriever


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--query", required=True); args = parser.parse_args()
    config = json.loads((ROOT / "configs" / "app_config.json").read_text(encoding="utf-8")); documents = json.loads((ROOT / "data" / "documents.json").read_text(encoding="utf-8"))
    for chunk in TfidfRetriever(build_chunks(documents, config["chunk_size"], config["chunk_overlap"])).search(args.query, config["top_k"]): print(f"{chunk['id']} | skor={chunk['score']:.3f} | {chunk['text']}")
