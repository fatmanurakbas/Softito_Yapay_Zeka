"""Hugging Face Trainer ile BERT duygu sınıflandırma fine-tuning betiği."""
from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Türkçe BERT fine-tuning")
    parser.add_argument("--model-name", default="dbmdz/bert-base-turkish-cased")
    parser.add_argument("--epochs", type=float, default=3)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--max-length", type=int, default=128)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        import numpy as np
        from datasets import load_dataset
        from transformers import AutoModelForSequenceClassification, AutoTokenizer, DataCollatorWithPadding, Trainer, TrainingArguments
    except ImportError as error:
        raise SystemExit("Önce `pip install -r requirements.txt` komutunu çalıştırın.") from error
    root = Path(__file__).resolve().parents[1]; processed = root / "data" / "processed"; output = root / "models" / "bert-sentiment"
    files = {split: str(processed / f"{split}.csv") for split in ("train", "validation", "test")}
    if not all(Path(path).exists() for path in files.values()): raise SystemExit("Önce `python 01-data-preparation/prepare_data.py` çalıştırın.")
    dataset = load_dataset("csv", data_files=files); tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    tokenized = dataset.map(lambda batch: tokenizer(batch["text"], truncation=True, max_length=args.max_length), batched=True)
    tokenized = tokenized.rename_column("label", "labels")
    model = AutoModelForSequenceClassification.from_pretrained(args.model_name, num_labels=2)
    def metrics(prediction):
        labels = prediction.label_ids; predicted = np.argmax(prediction.predictions, axis=1)
        accuracy = float((predicted == labels).mean()); f1_scores = []
        for label in (0, 1):
            tp = ((predicted == label) & (labels == label)).sum(); fp = ((predicted == label) & (labels != label)).sum(); fn = ((predicted != label) & (labels == label)).sum()
            precision, recall = tp / (tp + fp + 1e-9), tp / (tp + fn + 1e-9); f1_scores.append(2 * precision * recall / (precision + recall + 1e-9))
        return {"accuracy": accuracy, "macro_f1": float(np.mean(f1_scores))}
    training_args = TrainingArguments(output_dir=str(output), learning_rate=2e-5, per_device_train_batch_size=args.batch_size, per_device_eval_batch_size=args.batch_size, num_train_epochs=args.epochs, evaluation_strategy="epoch", save_strategy="epoch", load_best_model_at_end=True, metric_for_best_model="macro_f1", report_to="none", seed=42)
    trainer = Trainer(model=model, args=training_args, train_dataset=tokenized["train"], eval_dataset=tokenized["validation"], tokenizer=tokenizer, data_collator=DataCollatorWithPadding(tokenizer), compute_metrics=metrics)
    trainer.train(); print("Test metrikleri:", trainer.evaluate(tokenized["test"]))
    trainer.save_model(str(output)); tokenizer.save_pretrained(str(output))


if __name__ == "__main__": main()
