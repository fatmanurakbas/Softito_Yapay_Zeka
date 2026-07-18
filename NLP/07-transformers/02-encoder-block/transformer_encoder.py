"""NumPy ile sade Transformer encoder forward pass."""
from __future__ import annotations

import numpy as np


def layer_norm(values: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
    return (values - values.mean(axis=-1, keepdims=True)) / np.sqrt(values.var(axis=-1, keepdims=True) + epsilon)


def multi_head_attention(inputs: np.ndarray, heads: int, rng: np.random.Generator) -> tuple[np.ndarray, list[np.ndarray]]:
    dimension = inputs.shape[1]; head_dimension = dimension // heads; outputs, weights_per_head = [], []
    for _ in range(heads):
        wq, wk, wv = (rng.normal(0, 0.3, (dimension, head_dimension)) for _ in range(3))
        query, key, value = inputs @ wq, inputs @ wk, inputs @ wv
        scores = query @ key.T / np.sqrt(head_dimension); scores -= scores.max(axis=1, keepdims=True)
        weights = np.exp(scores); weights /= weights.sum(axis=1, keepdims=True)
        outputs.append(weights @ value); weights_per_head.append(weights)
    return np.concatenate(outputs, axis=1), weights_per_head


def encoder_block(inputs: np.ndarray, rng: np.random.Generator) -> tuple[np.ndarray, list[np.ndarray]]:
    attended, weights = multi_head_attention(inputs, heads=2, rng=rng)
    after_attention = layer_norm(inputs + attended)
    w1, w2 = rng.normal(0, 0.3, (8, 16)), rng.normal(0, 0.3, (16, 8))
    feed_forward = np.maximum(0, after_attention @ w1) @ w2
    return layer_norm(after_attention + feed_forward), weights


if __name__ == "__main__":
    tokens = ["bu", "ürün", "çok", "kaliteli"]; rng = np.random.default_rng(23)
    token_embeddings = rng.normal(0, 1, (len(tokens), 8))
    output, weights = encoder_block(token_embeddings, rng)
    print("Girdi şekli:", token_embeddings.shape, "| Çıktı şekli:", output.shape)
    print("Head 1, 'ürün' attention ağırlıkları:", dict(zip(tokens, np.round(weights[0][1], 3))))
    print("'ürün' için encoder çıktısı:", np.round(output[1], 3))
