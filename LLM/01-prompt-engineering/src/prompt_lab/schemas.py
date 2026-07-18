"""Yapılandırılmış LLM çıktılarını küçük, açık şemalarla doğrular."""
from __future__ import annotations

import json


def validate_output(task: str, raw_output: str) -> tuple[bool, str]:
    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError:
        return False, "Geçerli JSON değil."
    if task == "sentiment":
        if data.get("label") not in {"positive", "negative", "neutral"}: return False, "label geçersiz."
        if not isinstance(data.get("reason"), str) or not data["reason"].strip(): return False, "reason zorunludur."
        return True, "Geçerli."
    if task == "extraction":
        required = {"product", "issue", "resolution"}
        if set(data) != required: return False, "Alanlar şemayla eşleşmiyor."
        if not all(value is None or isinstance(value, str) for value in data.values()): return False, "Alan değerleri string veya null olmalı."
        return True, "Geçerli."
    return True, "Bu görev için yapılandırılmış şema yok."
