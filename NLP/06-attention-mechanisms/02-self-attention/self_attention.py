"""Scaled dot-product self-attention ve causal mask örneği."""
from __future__ import annotations

import numpy as np


def softmax_rows(scores: np.ndarray) -> np.ndarray:
    shifted = scores - scores.max(axis=1, keepdims=True)
    exp_scores = np.exp(shifted)
    return exp_scores / exp_scores.sum(axis=1, keepdims=True)


def self_attention(embeddings: np.ndarray, wq: np.ndarray, wk: np.ndarray, wv: np.ndarray, causal: bool = False) -> tuple[np.ndarray, np.ndarray]:
    query, key, value = embeddings @ wq, embeddings @ wk, embeddings @ wv
    scores = query @ key.T / np.sqrt(key.shape[1])
    if causal: scores = np.where(np.triu(np.ones_like(scores), k=1).astype(bool), -1e9, scores)
    weights = softmax_rows(scores)
    return weights @ value, weights


if __name__ == "__main__":
    tokens = ["ben", "bugün", "kitap", "okuyorum"]
    rng = np.random.default_rng(5); embeddings = rng.normal(size=(len(tokens), 6))
    output, weights = self_attention(embeddings, rng.normal(size=(6, 4)), rng.normal(size=(6, 4)), rng.normal(size=(6, 4)), causal=True)
    print("Causal attention matrisi (satır=query, sütun=key):")
    print("       " + " ".join(f"{token[:4]:>6}" for token in tokens))
    for token, row in zip(tokens, weights): print(f"{token[:6]:>6} " + " ".join(f"{value:6.2f}" for value in row))
    print("Output şekli:", output.shape)
