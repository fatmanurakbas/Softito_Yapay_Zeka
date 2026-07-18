"""Getirilen kaynakları açıkça sınırlayan RAG istemi."""
from __future__ import annotations


def build_rag_messages(question: str, chunks: list[dict]) -> list[dict[str, str]]:
    sources = "\n\n".join(f"[{chunk['id']}] {chunk['text']}" for chunk in chunks)
    system = "Sen Türkçe bir bilgi asistanısın. Yalnızca sağlanan kaynaklara dayan. Kaynakta yanıt yoksa bunu açıkça belirt. Yanıt sonunda kullandığın kaynak kimliklerini yaz."
    user = f"Kaynaklar:\n{sources}\n\nSoru: {question}"
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]
