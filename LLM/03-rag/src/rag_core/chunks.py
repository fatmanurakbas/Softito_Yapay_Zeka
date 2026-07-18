"""Belge metinlerini overlap'li token chunk'larına ayırır."""
from __future__ import annotations

import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü0-9]+", text.replace("İ", "i").replace("I", "ı").lower())


def build_chunks(documents: list[dict], chunk_size: int, overlap: int) -> list[dict]:
    if chunk_size < 1 or not 0 <= overlap < chunk_size: raise ValueError("chunk_size ve overlap geçersiz.")
    chunks = []
    for document in documents:
        words = tokenize(document["text"]); step = chunk_size - overlap
        for index, start in enumerate(range(0, len(words), step)):
            segment = words[start:start + chunk_size]
            if not segment: continue
            chunks.append({"id": f"{document['id']}-{index}", "document_id": document["id"], "title": document["title"], "text": " ".join(segment)})
            if start + chunk_size >= len(words): break
    return chunks
