"""İki head'li sade multi-head self-attention örneği."""
from __future__ import annotations

import numpy as np


def attention(query: np.ndarray, key: np.ndarray, value: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    scores = query @ key.T / np.sqrt(key.shape[1]); scores -= scores.max(axis=1, keepdims=True)
    weights = np.exp(scores); weights /= weights.sum(axis=1, keepdims=True)
    return weights @ value, weights


if __name__ == "__main__":
    tokens = ["kaliteli", "ürün", "hızlı", "kargo"]
    rng = np.random.default_rng(16); embeddings = rng.normal(size=(len(tokens), 8)); head_outputs = []
    for head in range(2):
        wq, wk, wv = (rng.normal(size=(8, 4)) for _ in range(3))
        output, weights = attention(embeddings @ wq, embeddings @ wk, embeddings @ wv); head_outputs.append(output)
        print(f"Head {head + 1} — 'ürün' tokenı ağırlıkları:", dict(zip(tokens, np.round(weights[1], 3))))
    combined = np.concatenate(head_outputs, axis=1)
    print("Birleştirilmiş çıktı şekli:", combined.shape)
