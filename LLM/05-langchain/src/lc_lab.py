"""Tüm örneklerin ortak LangChain/Ollama yapılandırması."""
from __future__ import annotations

import json
from pathlib import Path


def load_model(root: Path):
    try:
        from langchain_ollama import ChatOllama
    except ImportError as error:
        raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
    config = json.loads((root / "configs" / "app_config.json").read_text(encoding="utf-8"))
    if config["model"] == "your-local-model": raise SystemExit("configs/app_config.json içindeki model alanını değiştirin.")
    return ChatOllama(model=config["model"], base_url=config["base_url"], temperature=config["temperature"])
