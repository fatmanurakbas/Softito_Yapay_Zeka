"""Sinüzoidal positional encoding oluşturma örneği."""
from __future__ import annotations

import numpy as np


def positional_encoding(sequence_length: int, dimension: int) -> np.ndarray:
    positions = np.arange(sequence_length)[:, None]
    frequencies = np.exp(np.arange(0, dimension, 2) * -(np.log(10_000.0) / dimension))
    encoding = np.zeros((sequence_length, dimension))
    encoding[:, 0::2] = np.sin(positions * frequencies)
    encoding[:, 1::2] = np.cos(positions * frequencies)
    return encoding


if __name__ == "__main__":
    encoding = positional_encoding(sequence_length=5, dimension=8)
    for position, vector in enumerate(encoding): print(f"pozisyon {position}: {np.round(vector, 3)}")
