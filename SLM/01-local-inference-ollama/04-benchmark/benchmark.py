"""Ollama Chat API için basit warm-up ve token/saniye benchmark'ı."""
from __future__ import annotations

import argparse
import json
import time
from urllib.request import Request, urlopen


def request(base_url: str, model: str, prompt: str) -> dict:
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}], "stream": False}).encode("utf-8")
    http_request = Request(f"{base_url.rstrip('/')}/chat", data=body, headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(http_request, timeout=180) as response: return json.load(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--model", required=True); parser.add_argument("--runs", type=int, default=3); parser.add_argument("--prompt", default="Yerel çıkarımın faydalarını iki maddede açıkla."); parser.add_argument("--url", default="http://localhost:11434/api")
    args = parser.parse_args(); print("Warm-up isteği çalışıyor..."); request(args.url, args.model, args.prompt)
    throughputs = []
    for index in range(args.runs):
        started = time.perf_counter(); result = request(args.url, args.model, args.prompt); elapsed = time.perf_counter() - started
        generated, generation_seconds = result.get("eval_count", 0), result.get("eval_duration", 0) / 1e9
        tokens_per_second = generated / generation_seconds if generation_seconds else 0.0; throughputs.append(tokens_per_second)
        print(f"Çalıştırma {index + 1}: {elapsed:.2f} sn | {generated} token | {tokens_per_second:.2f} token/sn")
    print(f"Ortalama üretim hızı: {sum(throughputs) / len(throughputs):.2f} token/sn")
