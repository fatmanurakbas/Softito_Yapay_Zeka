from __future__ import annotations
import argparse,math
if __name__=="__main__":
 parser=argparse.ArgumentParser();parser.add_argument("--data-gb",type=float,required=True);parser.add_argument("--target-mb",type=float,default=256);args=parser.parse_args()
 if min(args.data_gb,args.target_mb)<=0:raise SystemExit("Değerler pozitif olmalıdır.")
 count=math.ceil(args.data_gb*1024/args.target_mb);print(f"Başlangıç partition önerisi: {count}");print("Bu bir başlangıç tahminidir; shuffle, sıkıştırma ve cluster paralelliğiyle doğrulayın.")
