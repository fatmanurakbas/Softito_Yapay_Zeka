"""Unigram, bigram ve trigram üretme örneği."""

from __future__ import annotations

import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zçğıöşü]+", text.lower())


def make_ngrams(tokens: list[str], n: int) -> list[str]:
    if n < 1:
        raise ValueError("n en az 1 olmalıdır.")
    return [" ".join(tokens[index:index + n]) for index in range(len(tokens) - n + 1)]


if __name__ == "__main__":
    tokens = tokenize("ürün çok kaliteli ve hızlı geldi")
    for n in (1, 2, 3):
        print(f"{n}-gram:", make_ngrams(tokens, n))
