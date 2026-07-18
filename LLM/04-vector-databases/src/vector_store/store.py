"""Eğitim amaçlı kalıcı JSON vektör deposu."""
from __future__ import annotations

import hashlib
import json
from math import sqrt
from pathlib import Path
import re


class HashingEmbedder:
    def __init__(self, dimension: int = 64) -> None: self.dimension = dimension
    def embed(self, text: str) -> list[float]:
        vector = [0.0] * self.dimension
        for token in re.findall(r"[a-zçğıöşü]+", text.replace("İ", "i").replace("I", "ı").lower()):
            index = int(hashlib.sha256(token.encode()).hexdigest(), 16) % self.dimension; vector[index] += 1
        norm = sqrt(sum(value * value for value in vector)); return [value / norm for value in vector] if norm else vector


class LocalVectorStore:
    def __init__(self, embedder: HashingEmbedder, records: list[dict] | None = None) -> None: self.embedder, self.records = embedder, records or []
    def upsert(self, document: dict) -> None:
        record = {**document, "vector": self.embedder.embed(document["text"])}; self.records = [item for item in self.records if item["id"] != document["id"]]; self.records.append(record)
    def search(self, query: str, top_k: int = 3, filters: dict[str, str] | None = None) -> list[dict]:
        query_vector = self.embedder.embed(query); filters = filters or {}; found = []
        for record in self.records:
            if any(record.get("metadata", {}).get(key) != value for key, value in filters.items()): continue
            score = sum(a * b for a, b in zip(query_vector, record["vector"])); found.append({**record, "score": round(score, 3)})
        return sorted(found, key=lambda item: item["score"], reverse=True)[:top_k]
    def save(self, path: str | Path) -> None: Path(path).write_text(json.dumps(self.records, ensure_ascii=False, indent=2), encoding="utf-8")
    @classmethod
    def load(cls, path: str | Path, embedder: HashingEmbedder) -> "LocalVectorStore": return cls(embedder, json.loads(Path(path).read_text(encoding="utf-8")))
