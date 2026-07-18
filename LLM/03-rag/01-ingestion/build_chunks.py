"""Örnek bilgi tabanından config ayarlarıyla chunk dosyası üretir."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from rag_core.chunks import build_chunks


if __name__ == "__main__":
    config = json.loads((ROOT / "configs" / "app_config.json").read_text(encoding="utf-8")); documents = json.loads((ROOT / "data" / "documents.json").read_text(encoding="utf-8"))
    chunks = build_chunks(documents, config["chunk_size"], config["chunk_overlap"]); (ROOT / "data" / "chunks.json").write_text(json.dumps(chunks, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(documents)} belge -> {len(chunks)} chunk üretildi.")
