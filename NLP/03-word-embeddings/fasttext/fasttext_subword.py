"""Karakter n-gramlarıyla sade FastText Skip-gram örneği."""
from __future__ import annotations

from pathlib import Path
import re
import numpy as np


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


def subwords(word: str) -> set[str]:
    wrapped = f"<{word}>"
    return {wrapped[index:index + size] for size in range(3, 6) for index in range(len(wrapped) - size + 1)}


def softmax(values: np.ndarray) -> np.ndarray:
    values = values - values.max(); exp_values = np.exp(values)
    return exp_values / exp_values.sum()


if __name__ == "__main__":
    corpus_path = Path(__file__).resolve().parents[1] / "data" / "corpus.txt"
    sentences = [tokens(line) for line in corpus_path.read_text(encoding="utf-8").splitlines()]
    words = sorted({word for sentence in sentences for word in sentence}); vocab = {word: index for index, word in enumerate(words)}
    ngrams = sorted({gram for word in words for gram in subwords(word)}); gram_index = {gram: index for index, gram in enumerate(ngrams)}
    word_grams = {word: [gram_index[gram] for gram in subwords(word)] for word in words}
    pairs = [(word, context) for sentence in sentences for position, word in enumerate(sentence)
             for context in sentence[max(0, position - 2):position] + sentence[position + 1:position + 3]]
    rng = np.random.default_rng(21); gram_vectors = rng.normal(0, 0.1, (len(ngrams), 16)); output = rng.normal(0, 0.1, (len(vocab), 16))
    for _ in range(250):
        for word, context_word in pairs:
            indices = word_grams[word]; center = gram_vectors[indices].mean(axis=0)
            error = softmax(output @ center); error[vocab[context_word]] -= 1
            center_gradient = error @ output
            output -= 0.04 * np.outer(error, center)
            gram_vectors[indices] -= 0.04 * center_gradient / len(indices)

    def vector(word: str) -> np.ndarray:
        indices = [gram_index[gram] for gram in subwords(word) if gram in gram_index]
        return gram_vectors[indices].mean(axis=0) if indices else np.zeros(16)
    def cosine(left: str, right: str) -> float:
        a, b = vector(left), vector(right)
        return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))

    print(f"Sözlük: {len(vocab)} | Karakter n-gramı: {len(ngrams)}")
    print("kitaplar alt-kelimeleri:", sorted(subwords("kitaplar"))[:8], "...")
    print(f"cosine(kitap, kitaplar) = {cosine('kitap', 'kitaplar'):.3f}")
    print(f"cosine(kitap, kitaplık) = {cosine('kitap', 'kitaplık'):.3f}  # eğitimde görülmeyen kelime")
