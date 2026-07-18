"""Türkçe sistem ve kullanıcı istemlerini güvenli, tutarlı biçimde üretir."""
from __future__ import annotations

import re


SYSTEM_PROMPT = """Sen Türkçe konuşan yardımcı bir küçük dil modelisin.
Yanıtlarını açık, kısa ve doğrudan ver. Bilmediğin bilgiyi uydurma.
Kullanıcı bağlam sağladıysa yalnızca bağlamdaki bilgiye dayan; yanıt yoksa bunu açıkça söyle."""


def normalize_turkish_text(text: str) -> str:
    """Türkçedeki I/İ dönüşümünü korur ve fazladan boşluğu temizler."""
    text = text.replace("İ", "i").replace("I", "ı").lower()
    return re.sub(r"\s+", " ", text).strip()


def build_user_prompt(question: str, context: str | None = None) -> str:
    question = question.strip()
    if not question:
        raise ValueError("Soru boş olamaz.")
    if not context or not context.strip():
        return question
    return f"Bağlam:\n---\n{context.strip()}\n---\n\nSoru: {question}\nYalnızca bağlama dayanarak yanıtla."
