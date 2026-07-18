from __future__ import annotations
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"src"))
from rag_eval.metrics import answer_metrics
if __name__=="__main__":
    cases={row["id"]:row for row in json.loads((ROOT/"data"/"evaluation_cases.json").read_text())}; retrieval={row["id"]:row["retrieved_sources"] for row in json.loads((ROOT/"data"/"retrieval_results.json").read_text())}; answers=json.loads((ROOT/"data"/"answer_results.json").read_text()); scores=[]
    for row in answers:
        score=answer_metrics(row["answer"],cases[row["id"]]["expected_keywords"],row["citations"],retrieval[row["id"]]);scores.append(score);print(row["id"],score)
    print("Ortalama yanıt uygunluğu:",round(sum(s["answer_relevance"] for s in scores)/len(scores),3))
