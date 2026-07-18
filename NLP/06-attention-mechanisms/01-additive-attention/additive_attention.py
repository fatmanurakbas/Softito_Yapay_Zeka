"""Bahdanau (additive) attention ile encoder durumlarını ağırlıklandırma."""
from __future__ import annotations

import numpy as np


def softmax(values: np.ndarray) -> np.ndarray:
    values = values - values.max()
    exponentials = np.exp(values)
    return exponentials / exponentials.sum()


def additive_attention(query: np.ndarray, encoder_states: np.ndarray, w_query: np.ndarray, w_key: np.ndarray, vector: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Context vector ve encoder zaman adımlarına ait attention ağırlıklarını döndürür."""
    energies = np.array([vector @ np.tanh(w_query @ query + w_key @ state) for state in encoder_states])
    weights = softmax(energies)
    return weights @ encoder_states, weights


if __name__ == "__main__":
    tokens = ["sipariş", "bugün", "hızlı", "teslim", "edildi"]
    rng = np.random.default_rng(8); encoder = rng.normal(size=(len(tokens), 4)); query = rng.normal(size=4)
    context, weights = additive_attention(query, encoder, rng.normal(size=(5, 4)), rng.normal(size=(5, 4)), rng.normal(size=5))
    for token, weight in zip(tokens, weights): print(f"{token:8} -> {weight:.3f}")
    print("Context vector:", np.round(context, 3))
