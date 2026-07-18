"""Ollama'nın yerel Chat API'si için hafif HTTP istemcisi."""
from __future__ import annotations

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class OllamaClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def chat(self, model: str, messages: list[dict[str, str]], options: dict[str, int | float], keep_alive: str) -> dict:
        body = json.dumps({"model": model, "messages": messages, "options": options, "keep_alive": keep_alive, "stream": False}).encode("utf-8")
        request = Request(f"{self.base_url}/chat", data=body, headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urlopen(request, timeout=180) as response: return json.load(response)
        except HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Ollama HTTP hatası {error.code}: {detail}") from error
        except URLError as error:
            raise RuntimeError("Ollama servisine ulaşılamadı. Uygulamanın çalıştığını kontrol edin.") from error
