"""TRL DPOTrainer ile tercih çiftlerinde DPO eğitimi."""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def main() -> None:
    try:
        from datasets import load_dataset
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from trl import DPOConfig, DPOTrainer
    except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
    cfg = json.loads((ROOT / "configs" / "dpo_config.json").read_text())
    if cfg["base_model"] == "your-base-model": raise SystemExit("configs/dpo_config.json içindeki base_model alanını değiştirin.")
    tokenizer = AutoTokenizer.from_pretrained(cfg["base_model"]); tokenizer.pad_token = tokenizer.pad_token or tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(cfg["base_model"]); reference_model = AutoModelForCausalLM.from_pretrained(cfg["base_model"])
    dataset = load_dataset("json", data_files=str(ROOT / "data" / "preferences.jsonl"), split="train")
    args = DPOConfig(output_dir=str(ROOT / cfg["output_dir"]), beta=cfg["beta"], num_train_epochs=cfg["epochs"], learning_rate=cfg["learning_rate"], per_device_train_batch_size=cfg["batch_size"], max_length=cfg["max_length"], max_prompt_length=cfg["max_prompt_length"], save_strategy="no", report_to="none")
    trainer = DPOTrainer(model=model, ref_model=reference_model, args=args, train_dataset=dataset, processing_class=tokenizer)
    trainer.train(); trainer.save_model(str(ROOT / cfg["output_dir"])); tokenizer.save_pretrained(ROOT / cfg["output_dir"])
if __name__ == "__main__": main()
