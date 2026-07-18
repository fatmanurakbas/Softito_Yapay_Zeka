"""NumPy ile BPTT kullanan küçük RNN duygu sınıflandırıcısı."""
from __future__ import annotations

import csv
from pathlib import Path
import re
import numpy as np


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


def sigmoid(value: float) -> float:
    return float(1 / (1 + np.exp(-np.clip(value, -30, 30))))


class SentimentRNN:
    def __init__(self, vocabulary_size: int, embedding_size: int = 12, hidden_size: int = 14) -> None:
        rng = np.random.default_rng(42)
        self.embeddings = rng.normal(0, 0.15, (vocabulary_size, embedding_size))
        self.wx = rng.normal(0, 0.15, (hidden_size, embedding_size))
        self.wh = rng.normal(0, 0.15, (hidden_size, hidden_size))
        self.bh = np.zeros(hidden_size)
        self.wo = rng.normal(0, 0.15, hidden_size)
        self.bo = 0.0

    def forward(self, sequence: list[int]) -> tuple[float, list[tuple[int, np.ndarray, np.ndarray]]]:
        hidden = np.zeros_like(self.bh)
        cache: list[tuple[int, np.ndarray, np.ndarray]] = []
        for token_id in sequence:
            previous = hidden.copy()
            hidden = np.tanh(self.wx @ self.embeddings[token_id] + self.wh @ hidden + self.bh)
            cache.append((token_id, previous, hidden))
        return sigmoid(self.wo @ hidden + self.bo), cache

    def train_one(self, sequence: list[int], label: int, learning_rate: float = 0.06) -> float:
        prediction, cache = self.forward(sequence)
        output_gradient = prediction - label
        grad_wo = output_gradient * cache[-1][2]; grad_bo = output_gradient
        grad_hidden = output_gradient * self.wo
        grad_embeddings = np.zeros_like(self.embeddings); grad_wx = np.zeros_like(self.wx)
        grad_wh = np.zeros_like(self.wh); grad_bh = np.zeros_like(self.bh)
        for token_id, previous, hidden in reversed(cache):
            raw_gradient = grad_hidden * (1 - hidden ** 2)
            grad_wx += np.outer(raw_gradient, self.embeddings[token_id])
            grad_wh += np.outer(raw_gradient, previous); grad_bh += raw_gradient
            grad_embeddings[token_id] += self.wx.T @ raw_gradient
            grad_hidden = self.wh.T @ raw_gradient
        for gradient in (grad_embeddings, grad_wx, grad_wh, grad_bh, grad_wo):
            np.clip(gradient, -5, 5, out=gradient)
        self.embeddings -= learning_rate * grad_embeddings; self.wx -= learning_rate * grad_wx
        self.wh -= learning_rate * grad_wh; self.bh -= learning_rate * grad_bh
        self.wo -= learning_rate * grad_wo; self.bo -= learning_rate * grad_bo
        return -(label * np.log(prediction + 1e-9) + (1 - label) * np.log(1 - prediction + 1e-9))

    def predict(self, sequence: list[int]) -> tuple[int, float]:
        probability, _ = self.forward(sequence)
        return int(probability >= 0.5), probability


if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1] / "data" / "sentiment.csv"
    with path.open(encoding="utf-8", newline="") as file:
        rows = [(int(row["label"]), tokenize(row["text"]), row["text"]) for row in csv.DictReader(file)]
    vocabulary = {word: index + 1 for index, word in enumerate(sorted({word for _, text, _ in rows for word in text}))}
    sequences = [(label, [vocabulary[word] for word in text], raw) for label, text, raw in rows]
    # Küçük veri setinde her sınıfın son örneğini testte tutarak dengeli bir ayrım yapıyoruz.
    positive = [sample for sample in sequences if sample[0] == 1]
    negative = [sample for sample in sequences if sample[0] == 0]
    train, test = positive[:-1] + negative[:-1], [positive[-1], negative[-1]]
    model = SentimentRNN(len(vocabulary) + 1)
    for epoch in range(180):
        losses = [model.train_one(sequence, label) for label, sequence, _ in train]
        if epoch in (0, 59, 119, 179):
            print(f"Epoch {epoch + 1:3}: ortalama kayıp = {np.mean(losses):.3f}")
    correct = 0
    for expected, sequence, text in test:
        predicted, probability = model.predict(sequence)
        correct += predicted == expected
        print(f"beklenen={expected} tahmin={predicted} olasılık={probability:.2f} | {text}")
    print(f"Test doğruluğu: {correct / len(test):.0%} ({len(test)} örnek)")
