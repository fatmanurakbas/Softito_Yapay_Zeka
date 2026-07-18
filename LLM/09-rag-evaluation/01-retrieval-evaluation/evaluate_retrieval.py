from __future__ import annotations
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from rag_eval.metrics import retrieval_metrics
if __name__=="__main__":
    cases={row["id"]:row for row in json.loads((ROOT/"data"/"evaluation_cases.json").read_text())}; results=json.loads((ROOT/"data"/"retrieval_results.json").read_text()); scores=[]
    for row in results:
        score=retrieval_metrics(cases[row["id"]]["gold_sources"],row["retrieved_sources"],3);scores.append(score);print(row["id"],score)
    print("Ortalama Recall@3:",round(sum(s["recall_at_k"] for s in scores)/len(scores),3))
