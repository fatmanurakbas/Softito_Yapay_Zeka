"""Ollama yerel Chat API istemcisi (harici paket gerektirmez)."""
from __future__ import annotations

import argparse
import json
from urllib.request import Request, urlopen


def chat(base_url: str, model: str, prompt: str, system: str | None = None) -> dict:
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
    body = json.dumps({"model": model, "messages": messages, "stream": False}).encode("utf-8")
    request = Request(f"{base_url.rstrip('/')}/chat", data=body, headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=180) as response: return json.load(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--model", required=True); parser.add_argument("--prompt", required=True); parser.add_argument("--system"); parser.add_argument("--url", default="http://localhost:11434/api")
    args = parser.parse_args(); result = chat(args.url, args.model, args.prompt, args.system)
    print(result["message"]["content"].strip())
    print(f"\nToplam süre: {result.get('total_duration', 0) / 1e9:.2f} sn | Üretilen token: {result.get('eval_count', 0)}")
