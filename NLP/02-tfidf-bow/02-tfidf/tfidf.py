"""Harici kütüphane olmadan TF-IDF hesaplama örneği."""

from __future__ import annotations

from collections import Counter
from math import log, sqrt
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


def fit_tfidf(documents: list[str]) -> tuple[list[str], dict[str, float]]:
    vocabulary = sorted({token for doc in documents for token in tokenize(doc)})
    document_frequency = Counter(token for doc in documents for token in set(tokenize(doc)))
    total_documents = len(documents)
    idf = {word: log((total_documents + 1) / (document_frequency[word] + 1)) + 1 for word in vocabulary}
    return vocabulary, idf


def transform(text: str, vocabulary: list[str], idf: dict[str, float]) -> list[float]:
    tokens = tokenize(text)
    counts = Counter(tokens)
    vector = [(counts[word] / len(tokens) if tokens else 0.0) * idf[word] for word in vocabulary]
    norm = sqrt(sum(value * value for value in vector))
    return [round(value / norm, 3) if norm else 0.0 for value in vector]


if __name__ == "__main__":
    documents = ["ürün kaliteli ve hızlı", "hızlı kargo ve özenli paketleme", "ürün kalitesi kötü"]
    vocabulary, idf = fit_tfidf(documents)
    print("Sözlük:", vocabulary)
    print("IDF   :", {word: round(value, 3) for word, value in idf.items()})
    for document in documents:
        print(f"{document!r} -> {transform(document, vocabulary, idf)}")
