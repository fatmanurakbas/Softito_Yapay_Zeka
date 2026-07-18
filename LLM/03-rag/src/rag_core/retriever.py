"""Şeffaf, küçük koleksiyonlar için TF-IDF cosine retriever."""
from __future__ import annotations

from collections import Counter
from math import log, sqrt
from .chunks import tokenize


class TfidfRetriever:
    def __init__(self, chunks: list[dict]) -> None:
        self.chunks = chunks; self.vocabulary = sorted({token for chunk in chunks for token in tokenize(chunk["text"])})
        document_frequency = Counter(token for chunk in chunks for token in set(tokenize(chunk["text"])))
        self.idf = {token: log((len(chunks) + 1) / (document_frequency[token] + 1)) + 1 for token in self.vocabulary}
        self.vectors = [self._vectorize(chunk["text"]) for chunk in chunks]

    def _vectorize(self, text: str) -> list[float]:
        counts = Counter(tokenize(text)); vector = [counts[token] * self.idf[token] for token in self.vocabulary]; norm = sqrt(sum(value * value for value in vector))
        return [value / norm for value in vector] if norm else vector

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        query_vector = self._vectorize(query); scored = [(sum(a * b for a, b in zip(query_vector, vector)), chunk) for vector, chunk in zip(self.vectors, self.chunks)]
        return [{**chunk, "score": round(score, 3)} for score, chunk in sorted(scored, key=lambda item: item[0], reverse=True)[:top_k]]
