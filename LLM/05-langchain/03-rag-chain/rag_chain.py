"""LCEL RunnableLambda ile hafif, şeffaf TF-IDF-benzeri anahtar kelime retrieval."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from lc_lab import load_model

def retrieve(question: str) -> str:
    docs = json.loads((ROOT / "data" / "documents.json").read_text(encoding="utf-8")); tokens = set(re.findall(r"[a-zçğıöşü]+", question.lower()))
    ranked = sorted(docs, key=lambda doc: len(tokens & set(re.findall(r"[a-zçğıöşü]+", doc["text"].lower()))), reverse=True)[:2]
    return "\n".join(f"[{doc['id']}] {doc['text']}" for doc in ranked)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--question", required=True); args = parser.parse_args()
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnableLambda, RunnablePassthrough
    prompt = ChatPromptTemplate.from_messages([("system", "Yalnızca bağlama dayanarak Türkçe yanıt ver; kaynak kimliğini belirt."), ("human", "Bağlam:\n{context}\n\nSoru: {question}")])
    chain = {"context": RunnableLambda(retrieve), "question": RunnablePassthrough()} | prompt | load_model(ROOT) | StrOutputParser()
    print(chain.invoke(args.question))
