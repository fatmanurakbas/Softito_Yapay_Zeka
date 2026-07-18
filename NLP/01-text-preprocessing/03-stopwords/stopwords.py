"""Göreve göre düzenlenebilen Türkçe stop word filtreleme örneği."""

from __future__ import annotations

TURKISH_STOPWORDS = {
    "acaba", "ama", "ancak", "bana", "bazı", "ben", "bir", "bu", "da", "de",
    "daha", "gibi", "için", "ile", "ki", "mi", "mı", "mu", "mü", "ne", "o",
    "olarak", "sadece", "şu", "ve", "veya", "ya", "yani",
}


def remove_stopwords(tokens: list[str], stopwords: set[str] = TURKISH_STOPWORDS) -> list[str]:
    """Stop word olmayan tokenları sıralarını koruyarak döndürür."""
    return [token for token in tokens if token not in stopwords]


if __name__ == "__main__":
    tokens = ["bu", "ürün", "çok", "iyi", "ama", "kargo", "gecikti"]
    print("Önce:", tokens)
    print("Sonra:", remove_stopwords(tokens))
