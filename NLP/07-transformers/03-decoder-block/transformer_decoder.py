"""Causal self-attention içeren sade Transformer decoder forward pass."""
from __future__ import annotations

import numpy as np


def causal_attention(inputs: np.ndarray, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    dimension = inputs.shape[1]; wq, wk, wv = (rng.normal(0, 0.25, (dimension, dimension)) for _ in range(3))
    query, key, value = inputs @ wq, inputs @ wk, inputs @ wv
    scores = query @ key.T / np.sqrt(dimension)
    scores[np.triu_indices_from(scores, k=1)] = -1e9
    scores -= scores.max(axis=1, keepdims=True); weights = np.exp(scores); weights /= weights.sum(axis=1, keepdims=True)
    return weights @ value, weights


if __name__ == "__main__":
    tokens = ["bugün", "kitap", "okumayı", "seviyorum"]; vocabulary = ["çok", "kitap", "seviyorum", "yarın", "okuyacağım"]
    rng = np.random.default_rng(31); embeddings = rng.normal(0, 1, (len(tokens), 8))
    attended, weights = causal_attention(embeddings, rng)
    residual = attended + embeddings; feed_forward = np.maximum(0, residual @ rng.normal(0, 0.25, (8, 16))) @ rng.normal(0, 0.25, (16, 8))
    logits = (residual + feed_forward) @ rng.normal(0, 0.25, (8, len(vocabulary)))
    print("Son token için izin verilen attention:", dict(zip(tokens, np.round(weights[-1], 3))))
    print("İlk tokenın geleceğe attention değerleri:", np.round(weights[0, 1:], 3))
    print("Sonraki-token logits şekli:", logits.shape)
    print("Son konumdaki en yüksek logit:", vocabulary[int(np.argmax(logits[-1]))])
