"""Aynı değerlendirme örneklerini aday yerel modellerde çalıştırır."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from llm_comparison.client import generate
from llm_comparison.scoring import score_response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--dry-run", action="store_true"); parser.add_argument("--output", default=str(ROOT / "reports" / "results.json")); args = parser.parse_args()
    config = json.loads((ROOT / "configs" / "models.json").read_text(encoding="utf-8")); cases = json.loads((ROOT / "data" / "evaluation_cases.json").read_text(encoding="utf-8"))
    if args.dry_run:
        for model in config["models"]:
            for case in cases: print(f"planlandı | model={model} | case={case['id']}")
        raise SystemExit(0)
    if any(name.startswith("your-local-model") for name in config["models"]): raise SystemExit("configs/models.json içindeki aday model adlarını değiştirin.")
    results = []
    for model in config["models"]:
        for case in cases:
            started = time.perf_counter(); response = generate(config["base_url"], model, case["system"], case["prompt"], config["temperature"], config["max_output_tokens"]); latency = time.perf_counter() - started
            output = response["message"]["content"].strip(); scores = score_response(case["task"], output, case["expected_keywords"])
            results.append({"model": model, "case_id": case["id"], "task": case["task"], "output": output, "latency_seconds": round(latency, 3), "generated_tokens": response.get("eval_count", 0), "scores": scores})
            print(f"tamamlandı | {model} | {case['id']} | skor={scores['automatic_score']}")
    output_path = Path(args.output); output_path.parent.mkdir(parents=True, exist_ok=True); output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
