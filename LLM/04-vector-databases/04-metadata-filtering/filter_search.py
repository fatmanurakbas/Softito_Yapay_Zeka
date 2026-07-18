from __future__ import annotations
import argparse, json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from vector_store import HashingEmbedder, LocalVectorStore
if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--query", required=True); parser.add_argument("--category", required=True); args = parser.parse_args(); config = json.loads((ROOT / "configs" / "config.json").read_text())
    store = LocalVectorStore.load(ROOT / "data" / "index.json", HashingEmbedder(config["dimension"]))
    for item in store.search(args.query, config["top_k"], {"category": args.category}): print(f"{item['id']} | {item['score']:.3f} | {item['text']}")
