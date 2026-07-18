"""Tek quant modu için prompt çıktılarını ve gecikmeyi JSON'a kaydeder."""
from __future__ import annotations
import argparse, json, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--mode", choices=["4bit","8bit"], required=True); args = parser.parse_args()
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
    cfg = json.loads((ROOT / "configs" / "quant_config.json").read_text()); prompts = json.loads((ROOT / "data" / "prompts.json").read_text())
    if cfg["base_model"] == "your-base-model": raise SystemExit("configs/quant_config.json içindeki base_model alanını değiştirin.")
    quant = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=cfg["use_double_quant"], bnb_4bit_compute_dtype=torch.bfloat16) if args.mode == "4bit" else BitsAndBytesConfig(load_in_8bit=True)
    model = AutoModelForCausalLM.from_pretrained(cfg["base_model"], device_map="auto", quantization_config=quant); tokenizer = AutoTokenizer.from_pretrained(cfg["base_model"]); rows=[]
    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device); started=time.perf_counter(); output=model.generate(**inputs,max_new_tokens=cfg["max_new_tokens"],do_sample=False); rows.append({"prompt":prompt,"output":tokenizer.decode(output[0],skip_special_tokens=True),"seconds":round(time.perf_counter()-started,3)})
    (ROOT / "results" / f"{args.mode}.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8"); print(f"{len(rows)} sonuç kaydedildi.")
