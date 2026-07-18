"""Çok sayıda küçük dosyanın NameNode metadata belleğine tahmini etkisi."""
from __future__ import annotations
import argparse
if __name__ == "__main__":
 parser=argparse.ArgumentParser();parser.add_argument("--files",type=int,required=True);parser.add_argument("--metadata-bytes",type=int,default=200);args=parser.parse_args()
 if min(args.files,args.metadata_bytes)<0:raise SystemExit("Değerler negatif olamaz.")
 total=args.files*args.metadata_bytes;print(f"Tahmini metadata: {total/1024**2:.2f} MiB ({args.files:,} dosya)");print("Çözüm seçenekleri: daha büyük dosyalar, compaction, Parquet/ORC ve uygun partition tasarımı.")
