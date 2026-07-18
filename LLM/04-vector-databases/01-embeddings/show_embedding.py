from __future__ import annotations
import argparse
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from vector_store import HashingEmbedder
if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--text", required=True); args = parser.parse_args()
    vector = HashingEmbedder().embed(args.text); print("Aktif boyutlar:", [(i, round(v, 3)) for i, v in enumerate(vector) if v])
