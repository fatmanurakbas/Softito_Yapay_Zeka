"""Yerel Ollama Chat API istemcisi."""
from __future__ import annotations

import json
from urllib.request import Request, urlopen


def chat(base_url: str, model: str, messages: list[dict[str, str]]) -> str:
    request = Request(f"{base_url.rstrip('/')}/chat", data=json.dumps({"model": model, "messages": messages, "stream": False, "options": {"temperature": 0.1}}).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=180) as response: return json.load(response)["message"]["content"].strip()
