"""GGUF dosyalarını boyut ve adlandırma bilgisine göre listeler."""
from __future__ import annotations

import argparse
from pathlib import Path
import re


def readable_size(size: int) -> str:
    return f"{size / 1024 ** 3:.2f} GB" if size >= 1024 ** 3 else f"{size / 1024 ** 2:.1f} MB"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--models-dir", default="models"); args = parser.parse_args()
    directory = Path(args.models_dir); files = sorted(directory.glob("*.gguf"))
    if not files: raise SystemExit(f"{directory} içinde GGUF dosyası bulunamadı.")
    for file in files:
        match = re.search(r"(?i)(q\d(?:_[a-z0-9]+)?|f16|f32|bf16)", file.stem)
        print(f"{file.name:50} | {readable_size(file.stat().st_size):>10} | {match.group(1).upper() if match else 'bilinmiyor'}")
