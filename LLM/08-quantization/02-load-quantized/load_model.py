"""BitsAndBytesConfig ile 4-bit veya 8-bit çıkarım modeli yükler."""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--mode", choices=["4bit","8bit"], required=True); args = parser.parse_args()
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
    cfg = json.loads((ROOT / "configs" / "quant_config.json").read_text())
    if cfg["base_model"] == "your-base-model": raise SystemExit("configs/quant_config.json içindeki base_model alanını değiştirin.")
    quant = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4" if cfg["use_nf4"] else "fp4", bnb_4bit_use_double_quant=cfg["use_double_quant"], bnb_4bit_compute_dtype=torch.bfloat16) if args.mode == "4bit" else BitsAndBytesConfig(load_in_8bit=True)
    model = AutoModelForCausalLM.from_pretrained(cfg["base_model"], device_map="auto", torch_dtype="auto", quantization_config=quant); tokenizer = AutoTokenizer.from_pretrained(cfg["base_model"])
    print(f"Yüklendi: {args.mode} | Bellek ayak izi: {model.get_memory_footprint() / 1024**3:.2f} GiB | Tokenizer: {tokenizer.__class__.__name__}")
