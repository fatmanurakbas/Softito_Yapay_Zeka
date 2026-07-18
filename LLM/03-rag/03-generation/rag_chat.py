"""Kaynakları getirir; çevrimdışı gösterir veya yerel modelden yanıt alır."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from rag_core.chunks import build_chunks
from rag_core.ollama import chat
from rag_core.prompts import build_rag_messages
from rag_core.retriever import TfidfRetriever


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--question", required=True); parser.add_argument("--offline", action="store_true"); args = parser.parse_args()
    config = json.loads((ROOT / "configs" / "app_config.json").read_text(encoding="utf-8")); documents = json.loads((ROOT / "data" / "documents.json").read_text(encoding="utf-8"))
    chunks = TfidfRetriever(build_chunks(documents, config["chunk_size"], config["chunk_overlap"])).search(args.question, config["top_k"]); messages = build_rag_messages(args.question, chunks)
    if args.offline: print(json.dumps({"sources": [chunk["id"] for chunk in chunks], "messages": messages}, ensure_ascii=False, indent=2))
    elif config["model"] == "your-local-model": raise SystemExit("configs/app_config.json içindeki model alanını değiştirin.")
    else: print(chat(config["base_url"], config["model"], messages))
