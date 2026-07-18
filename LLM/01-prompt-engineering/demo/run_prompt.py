"""Prompt şablonlarını çevrimdışı inceleyen veya yerel modele gönderen CLI."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from prompt_lab.ollama_client import chat
from prompt_lab.schemas import validate_output
from prompt_lab.templates import PromptTemplateStore


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Türkçe prompt laboratuvarı")
    parser.add_argument("--task", choices=["summary", "sentiment", "extraction"], required=True); parser.add_argument("--text", required=True); parser.add_argument("--offline", action="store_true")
    args = parser.parse_args(); config = json.loads((ROOT / "configs" / "app_config.json").read_text(encoding="utf-8"))
    messages = PromptTemplateStore(ROOT / "prompts" / "templates.json").render(args.task, text=args.text)
    if args.offline:
        print(json.dumps(messages, ensure_ascii=False, indent=2)); raise SystemExit(0)
    if config["model"] == "your-local-model": raise SystemExit("configs/app_config.json içindeki model alanını değiştirin.")
    result = chat(config["base_url"], config["model"], messages, config["temperature"], config["max_output_tokens"]); output = result["message"]["content"].strip()
    print(output)
    if args.task != "summary": print("\nŞema kontrolü:", validate_output(args.task, output))
