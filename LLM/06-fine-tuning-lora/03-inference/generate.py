"""Eğitilmiş LoRA adapter ile kısa Türkçe metin üretir."""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--prompt", required=True); args = parser.parse_args()
    try:
        from peft import PeftModel
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
    cfg = json.loads((ROOT / "configs" / "training_config.json").read_text()); adapter = ROOT / cfg["output_dir"]
    if not adapter.exists(): raise SystemExit("Adapter bulunamadı; önce eğitim betiğini çalıştırın.")
    tokenizer = AutoTokenizer.from_pretrained(adapter); model = PeftModel.from_pretrained(AutoModelForCausalLM.from_pretrained(cfg["base_model"]), adapter)
    inputs = tokenizer(f"### Talimat\nTürkçe, kısa yanıt ver.\n### Girdi\n{args.prompt}\n### Yanıt\n", return_tensors="pt")
    print(tokenizer.decode(model.generate(**inputs, max_new_tokens=100, do_sample=False)[0], skip_special_tokens=True))
