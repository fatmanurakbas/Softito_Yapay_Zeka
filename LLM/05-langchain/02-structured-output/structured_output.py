"""Pydantic şeması ve modelin structured output desteğiyle duygu sınıflandırma."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
from pydantic import BaseModel, Field
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from lc_lab import load_model

class Sentiment(BaseModel):
    label: str = Field(description="positive, negative veya neutral")
    reason: str = Field(description="Kısa Türkçe gerekçe")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--text", required=True); args = parser.parse_args()
    from langchain_core.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages([("system", "Türkçe yorumu sınıflandır."), ("human", "Yorum: {text}")])
    chain = prompt | load_model(ROOT).with_structured_output(Sentiment)
    print(chain.invoke({"text": args.text}).model_dump_json(indent=2))
