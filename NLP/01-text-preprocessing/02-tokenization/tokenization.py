"""Cümle ve kelime tokenization örneği."""

from __future__ import annotations

import re


def sentence_tokenize(text: str) -> list[str]:
    """Basit noktalama işaretlerine göre cümlelere ayırır."""
    return [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text) if sentence.strip()]


def word_tokenize(text: str) -> list[str]:
    """Türkçe harfleri, sayıları ve apostroflu sözcükleri token olarak çıkarır."""
    text = text.replace("İ", "i").replace("I", "ı").lower()
    text = text.translate(str.maketrans("âîû", "aiu"))
    return re.findall(r"[a-zçğıöşü0-9]+(?:'[a-zçğıöşü]+)?|<[^>]+>", text)


if __name__ == "__main__":
    sample = "Ankara'da hava güzel! NLP çalışmasına bugün başladık. E-posta: <email>"
    print("Cümleler:", sentence_tokenize(sample))
    print("Kelimeler :", word_tokenize(sample))
