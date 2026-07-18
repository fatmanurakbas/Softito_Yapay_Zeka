"""Fine-tuned BERT ile tek metin sınıflandırma."""
from __future__ import annotations

import argparse
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--text", required=True); args = parser.parse_args()
    try:
        import torch
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
    except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` komutunu çalıştırın.") from error
    model_path = Path(__file__).resolve().parents[1] / "models" / "bert-sentiment"
    if not model_path.exists(): raise SystemExit("Eğitilmiş model bulunamadı; önce eğitim betiğini çalıştırın.")
    tokenizer = AutoTokenizer.from_pretrained(model_path); model = AutoModelForSequenceClassification.from_pretrained(model_path); model.eval()
    with torch.no_grad(): probabilities = torch.softmax(model(**tokenizer(args.text, return_tensors="pt", truncation=True)).logits, dim=1)[0].tolist()
    label = "positive" if probabilities[1] >= probabilities[0] else "negative"
    print({"label": label, "negative": round(probabilities[0], 4), "positive": round(probabilities[1], 4)})
