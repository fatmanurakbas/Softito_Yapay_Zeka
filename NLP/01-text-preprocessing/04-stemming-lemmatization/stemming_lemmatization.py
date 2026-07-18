"""Eğitim amaçlı, sınırlı Türkçe kök bulma örneği."""

from __future__ import annotations

COMMON_SUFFIXES = (
    "lerinizden", "larımızdan", "lerimizden", "larınızdan", "leriniz", "larımız",
    "lerinin", "ların", "leri", "ları", "ler", "lar", "dan", "den", "dir", "dır",
    "dur", "dür", "im", "ım", "um", "üm", "de", "da", "in", "ın", "un", "ün",
)


def simple_turkish_stem(token: str) -> str:
    """Uzunluğu koruyarak yalnızca bilinen yaygın son eklerden birini keser."""
    for suffix in COMMON_SUFFIXES:
        if token.endswith(suffix) and len(token) - len(suffix) >= 3:
            return token[: -len(suffix)]
    return token


if __name__ == "__main__":
    words = ["kitaplar", "evlerinizden", "modelin", "çalışmalarımız", "veri"]
    for word in words:
        print(f"{word:18} -> {simple_turkish_stem(word)}")
