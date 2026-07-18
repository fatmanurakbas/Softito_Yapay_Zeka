"""BoW özellikleriyle Multinomial Naive Bayes metin sınıflandırması."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import log
from pathlib import Path
import csv
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


class MultinomialNaiveBayes:
    def fit(self, samples: list[tuple[str, str]]) -> None:
        self.class_documents = Counter(label for label, _ in samples)
        self.word_counts: dict[str, Counter[str]] = defaultdict(Counter)
        self.total_words = Counter()
        self.vocabulary: set[str] = set()
        for label, text in samples:
            words = tokenize(text)
            self.word_counts[label].update(words)
            self.total_words[label] += len(words)
            self.vocabulary.update(words)

    def predict(self, text: str) -> str:
        total_documents = sum(self.class_documents.values())
        scores: dict[str, float] = {}
        for label, document_count in self.class_documents.items():
            score = log(document_count / total_documents)
            denominator = self.total_words[label] + len(self.vocabulary)
            for word in tokenize(text):
                score += log((self.word_counts[label][word] + 1) / denominator)
            scores[label] = score
        return max(scores, key=scores.get)


def load_reviews(path: Path) -> list[tuple[str, str]]:
    with path.open(encoding="utf-8", newline="") as file:
        return [(row["label"], row["text"]) for row in csv.DictReader(file)]


if __name__ == "__main__":
    data_path = Path(__file__).resolve().parents[1] / "data" / "reviews.csv"
    reviews = load_reviews(data_path)
    train, test = reviews[:8], reviews[8:]
    model = MultinomialNaiveBayes()
    model.fit(train)

    correct = 0
    for expected, text in test:
        prediction = model.predict(text)
        correct += prediction == expected
        print(f"Beklenen={expected:8} Tahmin={prediction:8} | {text}")
    print(f"Doğruluk: {correct / len(test):.0%} ({len(test)} test örneği)")
