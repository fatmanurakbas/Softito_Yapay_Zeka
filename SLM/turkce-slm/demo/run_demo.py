"""Türkçe SLM demosunu komut satırından çalıştırır."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from turkce_slm import AppConfig, TurkishSLMService


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Yerel Türkçe SLM demosu")
    parser.add_argument("--question", required=True, help="Modele sorulacak soru")
    parser.add_argument("--context", help="İsteğe bağlı kaynak bağlam")
    parser.add_argument("--config", default=str(ROOT / "configs" / "app_config.json"))
    args = parser.parse_args()
    service = TurkishSLMService(AppConfig.from_file(args.config))
    response = service.answer(args.question, args.context)
    print(response["answer"])
    print(f"\nModel: {response['model']} | Süre: {response['total_seconds']} sn | Üretilen token: {response['generated_tokens']}")
