"""Türkçe metin için bağımsız, uçtan uca ön işleme pipeline'ı."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import unicodedata


STOPWORDS = {"ama", "ancak", "bir", "bu", "da", "de", "gibi", "için", "ile", "ki", "ve", "veya"}
SUFFIXES = ("ler", "lar", "leri", "ları", "dan", "den", "de", "da", "in", "ın", "un", "ün")


@dataclass(frozen=True)
class PreprocessingConfig:
    remove_stopwords: bool = True
    apply_stemming: bool = False
    keep_numbers: bool = True


def normalize(text: str) -> str:
    text = text.replace("İ", "i").replace("I", "ı").lower()
    text = unicodedata.normalize("NFC", text).translate(str.maketrans("âîû", "aiu"))
    text = re.sub(r"https?://\S+|www\.\S+", " <url> ", text)
    text = re.sub(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", " <email> ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str, keep_numbers: bool) -> list[str]:
    pattern = r"[a-zçğıöşü0-9]+(?:'[a-zçğıöşü]+)?|<[^>]+>" if keep_numbers else r"[a-zçğıöşü]+(?:'[a-zçğıöşü]+)?|<[^>]+>"
    return re.findall(pattern, text)


def stem(token: str) -> str:
    for suffix in SUFFIXES:
        if token.endswith(suffix) and len(token) - len(suffix) >= 3:
            return token[: -len(suffix)]
    return token


def preprocess(text: str, config: PreprocessingConfig = PreprocessingConfig()) -> list[str]:
    """Bir metni yapılandırılmış adımlarla token listesine dönüştürür."""
    tokens = tokenize(normalize(text), config.keep_numbers)
    if config.remove_stopwords:
        tokens = [token for token in tokens if token not in STOPWORDS]
    if config.apply_stemming:
        tokens = [stem(token) for token in tokens]
    return tokens


if __name__ == "__main__":
    data_path = Path(__file__).resolve().parents[1] / "data" / "sample_texts.txt"
    config = PreprocessingConfig(remove_stopwords=True, apply_stemming=False)
    for index, text in enumerate(data_path.read_text(encoding="utf-8").splitlines(), start=1):
        print(f"{index}. {preprocess(text, config)}")
