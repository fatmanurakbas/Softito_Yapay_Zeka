"""LSTM kapılarının bir forward pass içindeki davranışı."""
from __future__ import annotations

import numpy as np


def sigmoid(values: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-values))


def lstm_step(x_t: np.ndarray, h_prev: np.ndarray, c_prev: np.ndarray, wx: np.ndarray, wh: np.ndarray, bias: np.ndarray) -> tuple[np.ndarray, np.ndarray, tuple[np.ndarray, ...]]:
    hidden_size = len(h_prev)
    gates = wx @ x_t + wh @ h_prev + bias
    forget, input_gate, output = (sigmoid(part) for part in np.split(gates[: 3 * hidden_size], 3))
    candidate = np.tanh(gates[3 * hidden_size:])
    cell = forget * c_prev + input_gate * candidate
    hidden = output * np.tanh(cell)
    return hidden, cell, (forget, input_gate, output, candidate)


if __name__ == "__main__":
    rng = np.random.default_rng(10); hidden_size = 3
    wx = rng.normal(0, 0.4, (4 * hidden_size, 2)); wh = rng.normal(0, 0.4, (4 * hidden_size, hidden_size))
    hidden, cell = np.zeros(hidden_size), np.zeros(hidden_size)
    for step, x_t in enumerate((np.array([1.0, 0.0]), np.array([0.0, 1.0]), np.array([1.0, 1.0])), start=1):
        hidden, cell, (forget, input_gate, output, _) = lstm_step(x_t, hidden, cell, wx, wh, np.zeros(4 * hidden_size))
        print(f"t={step} forget={np.round(forget, 2)} input={np.round(input_gate, 2)} output={np.round(output, 2)}")
        print(f"     cell={np.round(cell, 3)} hidden={np.round(hidden, 3)}")
