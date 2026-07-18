"""LCEL ile en küçük prompt | model | parser zinciri."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from lc_lab import load_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--question", required=True); args = parser.parse_args()
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages([("system", "Türkçe, kısa ve doğru yanıt ver."), ("human", "{question}")])
    chain = prompt | load_model(ROOT) | StrOutputParser()
    print(chain.invoke({"question": args.question}))
