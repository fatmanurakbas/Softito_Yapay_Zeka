"""Bir RNN hücresinin zaman adımları boyunca forward pass örneği."""
from __future__ import annotations

import numpy as np


def rnn_step(x_t: np.ndarray, h_previous: np.ndarray, wx: np.ndarray, wh: np.ndarray, bias: np.ndarray) -> np.ndarray:
    """Tek bir zaman adımı için yeni gizli durumu döndürür."""
    return np.tanh(wx @ x_t + wh @ h_previous + bias)


if __name__ == "__main__":
    inputs = [np.array([1.0, 0.0]), np.array([0.0, 1.0]), np.array([1.0, 1.0])]
    wx = np.array([[0.5, -0.2], [0.1, 0.4], [-0.3, 0.2]])
    wh = np.array([[0.3, 0.0, 0.1], [0.0, 0.2, 0.1], [0.1, -0.1, 0.2]])
    hidden = np.zeros(3)
    for step, x_t in enumerate(inputs, start=1):
        hidden = rnn_step(x_t, hidden, wx, wh, np.zeros(3))
        print(f"t={step}: h_t = {np.round(hidden, 3)}")
