from __future__ import annotations
from collections import Counter
if __name__=="__main__":
 keys=["anonim"]*800+[f"user-{i}" for i in range(200)];counts=Counter(keys);largest=counts.most_common(1)[0]
 print(f"Farklı anahtar: {len(counts)} | En büyük anahtar: {largest}");print(f"En büyük anahtarın veri payı: {largest[1]/len(keys):.1%}");print("Olası çözümler: salting, ön toplulaştırma, broadcast dimension ve AQE skew join.")
