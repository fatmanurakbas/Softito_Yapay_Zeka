"""Türkçe metin normalleştirme örneği."""

from __future__ import annotations

import re
import unicodedata


def normalize_text(text: str) -> str:
    """Metni modellemeye uygun, tutarlı bir biçime getirir."""
    text = text.replace("İ", "i").replace("I", "ı").lower()
    text = unicodedata.normalize("NFC", text).translate(str.maketrans("âîû", "aiu"))
    text = re.sub(r"https?://\S+|www\.\S+", " <url> ", text)
    text = re.sub(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", " <email> ", text)
    text = re.sub(r"\b\d{1,3}(?:\.\d{3})*(?:,\d+)?\s*(?:tl|₺)\b", " <money> ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


if __name__ == "__main__":
    raw_text = "Merhaba! Bilgi@Softito.example adresine yazın; fiyat 1.250,50 TL. https://softito.example"
    print("Ham metin :", raw_text)
    print("Normalize :", normalize_text(raw_text))
