"""Küçük derlem için sade GloVe eğitimi ve birlikte-görünme matrisi."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re
import numpy as np


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


if __name__ == "__main__":
    corpus_path = Path(__file__).resolve().parents[1] / "data" / "corpus.txt"
    sentences = [tokens(line) for line in corpus_path.read_text(encoding="utf-8").splitlines()]
    words = sorted({word for sentence in sentences for word in sentence})
    vocab = {word: index for index, word in enumerate(words)}
    cooccurrence: dict[tuple[int, int], float] = defaultdict(float)
    for sentence in sentences:
        for index, word in enumerate(sentence):
            for other_index in range(max(0, index - 2), min(len(sentence), index + 3)):
                if index != other_index:
                    cooccurrence[vocab[word], vocab[sentence[other_index]]] += 1 / abs(index - other_index)

    rng = np.random.default_rng(7)
    main = rng.normal(0, 0.1, (len(vocab), 12)); context = rng.normal(0, 0.1, (len(vocab), 12))
    main_bias = np.zeros(len(vocab)); context_bias = np.zeros(len(vocab))
    for _ in range(120):
        for (left, right), count in cooccurrence.items():
            weight = min(1.0, (count / 10) ** 0.75)
            error = main[left] @ context[right] + main_bias[left] + context_bias[right] - np.log(count)
            gradient = 0.04 * weight * error
            left_vector, right_vector = main[left].copy(), context[right].copy()
            main[left] -= gradient * right_vector; context[right] -= gradient * left_vector
            main_bias[left] -= gradient; context_bias[right] -= gradient

    print(f"Sözlük: {len(vocab)} kelime | Birlikte-görünme çifti: {len(cooccurrence)}")
    for left, right in (("ürün", "iyi"), ("kamera", "fotoğraf"), ("kitap", "öğrenci")):
        print(f"cooc({left}, {right}) = {cooccurrence[vocab[left], vocab[right]]:.2f}")
