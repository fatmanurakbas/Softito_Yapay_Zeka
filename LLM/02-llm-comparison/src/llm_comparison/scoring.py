"""Yanıtların temel otomatik kalite/biçim metrikleri."""
from __future__ import annotations

from collections import defaultdict
import json


def score_response(task: str, output: str, expected_keywords: list[str]) -> dict[str, float | bool]:
    normalized = output.lower(); coverage = sum(keyword.lower() in normalized for keyword in expected_keywords) / len(expected_keywords) if expected_keywords else 1.0
    json_valid = True
    if task == "structured":
        try:
            data = json.loads(output); json_valid = data.get("label") in {"positive", "negative", "neutral"} and isinstance(data.get("reason"), str)
        except json.JSONDecodeError: json_valid = False
    return {"keyword_coverage": round(coverage, 3), "json_valid": json_valid, "automatic_score": round(coverage * (1.0 if json_valid else 0.0), 3)}


def summarize_results(rows: list[dict]) -> list[dict[str, float | str]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in rows: groups[row["model"]].append(row)
    summary = []
    for model, items in groups.items():
        summary.append({"model": model, "cases": len(items), "mean_score": round(sum(item["scores"]["automatic_score"] for item in items) / len(items), 3), "mean_latency_seconds": round(sum(item["latency_seconds"] for item in items) / len(items), 3), "json_valid_rate": round(sum(item["scores"]["json_valid"] for item in items) / len(items), 3)})
    return sorted(summary, key=lambda row: (-row["mean_score"], row["mean_latency_seconds"]))
