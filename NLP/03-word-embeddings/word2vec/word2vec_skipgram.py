"""Küçük Türkçe derlemde NumPy ile Skip-gram Word2Vec eğitimi."""
from __future__ import annotations

from pathlib import Path
import re
import numpy as np


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


def softmax(values: np.ndarray) -> np.ndarray:
    shifted = values - values.max()
    exp_values = np.exp(shifted)
    return exp_values / exp_values.sum()


def similar(word: str, vectors: np.ndarray, vocab: dict[str, int], top_n: int = 4) -> list[tuple[str, float]]:
    unit = vectors / (np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-9)
    scores = unit @ unit[vocab[word]]
    ranked = ((item, float(scores[index])) for item, index in vocab.items() if item != word)
    return [(item, round(score, 3)) for item, score in sorted(ranked, key=lambda pair: pair[1], reverse=True)[:top_n]]


if __name__ == "__main__":
    corpus_path = Path(__file__).resolve().parents[1] / "data" / "corpus.txt"
    sentences = [tokens(line) for line in corpus_path.read_text(encoding="utf-8").splitlines()]
    vocabulary = sorted({word for sentence in sentences for word in sentence})
    vocab = {word: index for index, word in enumerate(vocabulary)}
    pairs = [(vocab[word], vocab[context]) for sentence in sentences for position, word in enumerate(sentence)
             for context in sentence[max(0, position - 2):position] + sentence[position + 1:position + 3]]

    rng = np.random.default_rng(42)
    input_vectors = rng.normal(0, 0.1, (len(vocab), 16))
    output_vectors = rng.normal(0, 0.1, (len(vocab), 16))
    for _ in range(350):
        for center, context in pairs:
            center_vector = input_vectors[center].copy()
            probabilities = softmax(output_vectors @ center_vector)
            probabilities[context] -= 1.0
            output_vectors -= 0.05 * np.outer(probabilities, center_vector)
            input_vectors[center] -= 0.05 * (probabilities @ output_vectors)

    print(f"Sözlük: {len(vocab)} kelime | Eğitim çifti: {len(pairs)}")
    for query in ("ürün", "kitap", "kamera"):
        print(f"{query:7} -> {similar(query, input_vectors, vocab)}")
