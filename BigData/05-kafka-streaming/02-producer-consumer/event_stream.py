"""Producer, offset ve consumer akışının küçük simülasyonu."""
from __future__ import annotations
events=[{"key":"u1","event":"view"},{"key":"u2","event":"add_cart"},{"key":"u1","event":"purchase"}]
if __name__=="__main__":
 for offset,event in enumerate(events):print(f"produce offset={offset}: {event}")
 committed=-1
 for offset,event in enumerate(events):
  print(f"consume offset={offset}: {event}");committed=offset
 print("Committed offset:",committed,"| yeniden başlatmada sonraki offset'ten devam edilir.")
