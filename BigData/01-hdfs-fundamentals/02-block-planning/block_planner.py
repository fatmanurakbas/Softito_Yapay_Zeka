"""HDFS blok sayısı ve replikasyon depolama maliyetini hesaplar."""
from __future__ import annotations
import argparse
import math
if __name__ == "__main__":
 parser=argparse.ArgumentParser();parser.add_argument("--file-mb",type=float,required=True);parser.add_argument("--block-mb",type=float,default=128);parser.add_argument("--replication",type=int,default=3);args=parser.parse_args()
 if min(args.file_mb,args.block_mb,args.replication)<=0:raise SystemExit("Tüm değerler pozitif olmalıdır.")
 blocks=math.ceil(args.file_mb/args.block_mb);print(f"Blok sayısı: {blocks}");print(f"Mantıksal boyut: {args.file_mb:.1f} MB");print(f"Replikalı fiziksel boyut: {args.file_mb*args.replication:.1f} MB")
