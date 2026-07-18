"""Yerel Ollama Chat API çağrısı."""
from __future__ import annotations

import json
from urllib.request import Request, urlopen


def chat(base_url: str, model: str, messages: list[dict[str, str]], temperature: float, max_output_tokens: int) -> dict:
    payload = {"model": model, "messages": messages, "options": {"temperature": temperature, "num_predict": max_output_tokens}, "stream": False}
    request = Request(f"{base_url.rstrip('/')}/chat", data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=180) as response: return json.load(response)
