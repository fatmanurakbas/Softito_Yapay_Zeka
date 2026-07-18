"""Causal LM üzerinde PEFT LoRA adapter eğitimi."""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def main() -> None:
    try:
        from datasets import load_dataset
        from peft import LoraConfig, TaskType, get_peft_model
        from transformers import AutoModelForCausalLM, AutoTokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments
    except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
    cfg = json.loads((ROOT / "configs" / "training_config.json").read_text())
    if cfg["base_model"] == "your-base-model": raise SystemExit("configs/training_config.json içindeki base_model alanını değiştirin.")
    tokenizer = AutoTokenizer.from_pretrained(cfg["base_model"]); tokenizer.pad_token = tokenizer.pad_token or tokenizer.eos_token
    data = load_dataset("json", data_files=str(ROOT / "data" / "train.jsonl"), split="train")
    def format_row(row): return f"### Talimat\n{row['instruction']}\n### Girdi\n{row['input']}\n### Yanıt\n{row['output']}"
    tokenized = data.map(lambda batch: tokenizer([format_row(row) for row in [{key: batch[key][i] for key in batch} for i in range(len(batch['input']))]], truncation=True, max_length=cfg["max_length"]), batched=True, remove_columns=data.column_names)
    model = AutoModelForCausalLM.from_pretrained(cfg["base_model"])
    lora = LoraConfig(task_type=TaskType.CAUSAL_LM, r=cfg["r"], lora_alpha=cfg["lora_alpha"], lora_dropout=cfg["lora_dropout"], target_modules=cfg["target_modules"])
    model = get_peft_model(model, lora); model.print_trainable_parameters()
    args = TrainingArguments(output_dir=str(ROOT / cfg["output_dir"]), num_train_epochs=cfg["epochs"], learning_rate=cfg["learning_rate"], per_device_train_batch_size=cfg["batch_size"], save_strategy="no", report_to="none")
    Trainer(model=model, args=args, train_dataset=tokenized, data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False)).train()
    model.save_pretrained(ROOT / cfg["output_dir"]); tokenizer.save_pretrained(ROOT / cfg["output_dir"])
if __name__ == "__main__": main()
