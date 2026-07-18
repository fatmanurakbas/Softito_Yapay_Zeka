"""Türkçe belgeler için basit Bag of Words vektörleştirme."""

from __future__ import annotations

from collections import Counter
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


def build_vocabulary(documents: list[str]) -> list[str]:
    return sorted({token for document in documents for token in tokenize(document)})


def count_vector(text: str, vocabulary: list[str]) -> list[int]:
    counts = Counter(tokenize(text))
    return [counts[word] for word in vocabulary]


if __name__ == "__main__":
    documents = ["ürün kaliteli ve hızlı", "hızlı kargo ve özenli paketleme", "ürün kalitesi kötü"]
    vocabulary = build_vocabulary(documents)
    print("Sözlük:", vocabulary)
    for document in documents:
        print(f"{document!r} -> {count_vector(document, vocabulary)}")
