"""llama-cli ile GGUF quant sürümleri için tekrar edilebilir duvar saati ölçümü."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import time


def run(cli: str, model: str, prompt: str, tokens: int) -> float:
    started = time.perf_counter()
    subprocess.run([cli, "-m", model, "-p", prompt, "-n", str(tokens), "--no-display-prompt"], check=True, capture_output=True, text=True)
    return time.perf_counter() - started


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--model", required=True); parser.add_argument("--cli", default="llama-cli"); parser.add_argument("--runs", type=int, default=3); parser.add_argument("--tokens", type=int, default=64); parser.add_argument("--prompt", default="Yerel yapay zekanın faydalarını iki maddede açıkla."); parser.add_argument("--output", default="results/benchmarks.csv")
    args = parser.parse_args(); model = Path(args.model)
    if not model.is_file(): raise SystemExit(f"Model bulunamadı: {model}")
    print("Warm-up çalışıyor..."); run(args.cli, str(model), args.prompt, args.tokens)
    output = Path(args.output); output.parent.mkdir(parents=True, exist_ok=True); new_file = not output.exists()
    with output.open("a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "model", "tokens", "run", "wall_seconds", "approx_tokens_per_second"])
        if new_file: writer.writeheader()
        for index in range(1, args.runs + 1):
            seconds = run(args.cli, str(model), args.prompt, args.tokens); throughput = args.tokens / seconds
            writer.writerow({"timestamp": datetime.now(timezone.utc).isoformat(), "model": model.name, "tokens": args.tokens, "run": index, "wall_seconds": f"{seconds:.3f}", "approx_tokens_per_second": f"{throughput:.2f}"})
            print(f"Çalıştırma {index}: {seconds:.2f} sn | yaklaşık {throughput:.2f} token/sn")
