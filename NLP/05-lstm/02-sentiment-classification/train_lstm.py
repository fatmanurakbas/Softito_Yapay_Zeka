"""NumPy ile BPTT kullanan küçük LSTM duygu sınıflandırıcısı."""
from __future__ import annotations

import csv
from pathlib import Path
import re
import numpy as np


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


def sigmoid(value: np.ndarray | float) -> np.ndarray | float:
    return 1 / (1 + np.exp(-np.clip(value, -30, 30)))


class SentimentLSTM:
    def __init__(self, vocab_size: int, embed_size: int = 12, hidden_size: int = 14) -> None:
        rng = np.random.default_rng(12); self.hidden_size = hidden_size
        self.embedding = rng.normal(0, 0.12, (vocab_size, embed_size))
        self.wx = rng.normal(0, 0.12, (4 * hidden_size, embed_size)); self.wh = rng.normal(0, 0.12, (4 * hidden_size, hidden_size))
        self.bias = np.zeros(4 * hidden_size); self.wo = rng.normal(0, 0.12, hidden_size); self.bo = 0.0

    def forward(self, sequence: list[int]) -> tuple[float, list[tuple[object, ...]]]:
        hidden = np.zeros(self.hidden_size); cell = np.zeros(self.hidden_size); cache = []
        for token_id in sequence:
            h_prev, c_prev = hidden.copy(), cell.copy(); x = self.embedding[token_id]
            gates = self.wx @ x + self.wh @ hidden + self.bias
            forget, input_gate, output = (sigmoid(part) for part in np.split(gates[: 3 * self.hidden_size], 3))
            candidate = np.tanh(gates[3 * self.hidden_size:]); cell = forget * cell + input_gate * candidate
            hidden = output * np.tanh(cell)
            cache.append((token_id, h_prev, c_prev, hidden, cell, forget, input_gate, output, candidate))
        return float(sigmoid(self.wo @ hidden + self.bo)), cache

    def train_one(self, sequence: list[int], label: int, lr: float = 0.05) -> float:
        probability, cache = self.forward(sequence); output_error = probability - label
        grad_embedding = np.zeros_like(self.embedding); grad_wx = np.zeros_like(self.wx); grad_wh = np.zeros_like(self.wh); grad_bias = np.zeros_like(self.bias)
        grad_wo = output_error * cache[-1][3]; grad_hidden = output_error * self.wo; grad_cell = np.zeros(self.hidden_size)
        for token_id, h_prev, c_prev, hidden, cell, forget, input_gate, output, candidate in reversed(cache):
            tanh_cell = np.tanh(cell); d_output = grad_hidden * tanh_cell
            d_cell = grad_hidden * output * (1 - tanh_cell ** 2) + grad_cell
            d_forget, d_input, d_candidate = d_cell * c_prev, d_cell * candidate, d_cell * input_gate
            grad_cell = d_cell * forget
            dz = np.concatenate((d_forget * forget * (1 - forget), d_input * input_gate * (1 - input_gate), d_output * output * (1 - output), d_candidate * (1 - candidate ** 2)))
            grad_wx += np.outer(dz, self.embedding[token_id]); grad_wh += np.outer(dz, h_prev); grad_bias += dz
            grad_embedding[token_id] += self.wx.T @ dz; grad_hidden = self.wh.T @ dz
        for gradient in (grad_embedding, grad_wx, grad_wh, grad_bias, grad_wo): np.clip(gradient, -5, 5, out=gradient)
        self.embedding -= lr * grad_embedding; self.wx -= lr * grad_wx; self.wh -= lr * grad_wh; self.bias -= lr * grad_bias
        self.wo -= lr * grad_wo; self.bo -= lr * output_error
        return float(-(label * np.log(probability + 1e-9) + (1 - label) * np.log(1 - probability + 1e-9)))

    def predict(self, sequence: list[int]) -> tuple[int, float]:
        probability, _ = self.forward(sequence); return int(probability >= 0.5), probability


if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1] / "data" / "sentiment.csv"
    with path.open(encoding="utf-8", newline="") as file: rows = [(int(row["label"]), tokenize(row["text"]), row["text"]) for row in csv.DictReader(file)]
    vocab = {word: index + 1 for index, word in enumerate(sorted({word for _, text, _ in rows for word in text}))}
    data = [(label, [vocab[word] for word in text], raw) for label, text, raw in rows]
    positive, negative = [row for row in data if row[0] == 1], [row for row in data if row[0] == 0]
    train, test = positive[:-1] + negative[:-1], [positive[-1], negative[-1]]; model = SentimentLSTM(len(vocab) + 1)
    for epoch in range(200):
        losses = [model.train_one(sequence, label) for label, sequence, _ in train]
        if epoch in (0, 79, 159, 199): print(f"Epoch {epoch + 1:3}: ortalama kayıp = {np.mean(losses):.3f}")
    correct = 0
    for expected, sequence, text in test:
        predicted, probability = model.predict(sequence); correct += predicted == expected
        print(f"beklenen={expected} tahmin={predicted} olasılık={probability:.2f} | {text}")
    print(f"Test doğruluğu: {correct / len(test):.0%} ({len(test)} örnek)")
