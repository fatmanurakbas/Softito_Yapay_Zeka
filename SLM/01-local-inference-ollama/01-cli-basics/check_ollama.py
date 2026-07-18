"""Ollama yerel API erişimini ve indirilen modelleri kontrol eder."""
from __future__ import annotations

import argparse
import json
from urllib.error import URLError
from urllib.request import urlopen


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--url", default="http://localhost:11434/api"); args = parser.parse_args()
    try:
        with urlopen(f"{args.url.rstrip('/')}/tags", timeout=5) as response: payload = json.load(response)
    except URLError as error:
        raise SystemExit(f"Ollama API'ye ulaşılamadı: {error.reason}") from error
    models = payload.get("models", [])
    print(f"Ollama erişilebilir. Yerel model sayısı: {len(models)}")
    for model in models:
        details = model.get("details", {})
        print(f"- {model['name']} | {model.get('size', 0) / 1e9:.2f} GB | {details.get('quantization_level', 'bilinmiyor')}")
