"""TF-IDF ve cosine similarity ile küçük belge araması."""

from __future__ import annotations

from collections import Counter
from math import log, sqrt
import re


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


def cosine(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right))
    denominator = sqrt(sum(a * a for a in left)) * sqrt(sum(b * b for b in right))
    return numerator / denominator if denominator else 0.0


def search(query: str, documents: list[str]) -> list[tuple[float, str]]:
    vocabulary = sorted({token for document in documents + [query] for token in tokens(document)})
    df = Counter(token for document in documents for token in set(tokens(document)))
    idf = {word: log((len(documents) + 1) / (df[word] + 1)) + 1 for word in vocabulary}

    def vectorize(text: str) -> list[float]:
        counts = Counter(tokens(text))
        return [counts[word] * idf[word] for word in vocabulary]

    query_vector = vectorize(query)
    return sorted(((cosine(query_vector, vectorize(document)), document) for document in documents), reverse=True)


if __name__ == "__main__":
    corpus = [
        "Kargo takip numarası ile sipariş durumunu öğrenin",
        "Telefon kamerası düşük ışıkta iyi sonuç veriyor",
        "İade sürecinde müşteri hizmetleri yardımcı oldu",
    ]
    for score, document in search("sipariş kargo durumu", corpus):
        print(f"{score:.3f} | {document}")
