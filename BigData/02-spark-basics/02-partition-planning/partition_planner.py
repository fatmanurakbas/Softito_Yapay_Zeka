"""Dosya boyutlarına göre partition yük dengesini gösterir."""
from __future__ import annotations
import math
def plan(files_mb:list[int],target_mb:int)->list[int]:
 loads=[0]*math.ceil(sum(files_mb)/target_mb)
 for size in sorted(files_mb,reverse=True):loads[loads.index(min(loads))]+=size
 return loads
if __name__=="__main__":
 files=[300,250,180,150,120,80,60,40];loads=plan(files,256);print("Partition yükleri (MB):",loads);print("Skew oranı:",round(max(loads)/min(loads),2))
