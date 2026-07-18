from __future__ import annotations
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from vector_store import HashingEmbedder, LocalVectorStore
if __name__ == "__main__":
    config = json.loads((ROOT / "configs" / "config.json").read_text()); documents = json.loads((ROOT / "data" / "documents.json").read_text(encoding="utf-8")); store = LocalVectorStore(HashingEmbedder(config["dimension"]))
    for document in documents: store.upsert(document)
    store.save(ROOT / "data" / "index.json"); print(f"{len(store.records)} belge indekslendi.")
