"""RAG retrieval ve yanıt metrikleri."""
from __future__ import annotations

def retrieval_metrics(gold: list[str], retrieved: list[str], k: int) -> dict[str, float]:
    top = retrieved[:k]; hits = len(set(gold) & set(top))
    return {"recall_at_k": hits / len(gold) if gold else 0.0, "context_precision": hits / len(top) if top else 0.0}

def answer_metrics(answer: str, expected_keywords: list[str], citations: list[str], retrieved: list[str]) -> dict[str, float]:
    normalized = answer.lower(); relevance = sum(keyword.lower() in normalized for keyword in expected_keywords) / len(expected_keywords) if expected_keywords else 1.0
    faithfulness = sum(citation in retrieved for citation in citations) / len(citations) if citations else 0.0
    return {"answer_relevance": relevance, "citation_faithfulness": faithfulness}
