"""Kafka benzeri tutarlı anahtar-partition eşleme örneği."""
from __future__ import annotations
import hashlib
def partition(key:str,count:int)->int:return int(hashlib.sha256(key.encode()).hexdigest(),16)%count
if __name__=="__main__":
 for key in ["user-1","user-2","user-1","order-9"]:print(f"{key:8} -> partition {partition(key,3)}")
 print("Aynı anahtar aynı partition'a gider; bu anahtar içi sıralamayı korur.")
