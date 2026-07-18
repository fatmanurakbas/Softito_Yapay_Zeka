from __future__ import annotations
tasks={"extract":[],"validate":["extract"],"transform":["validate"],"load":["transform"],"notify":["load"]}
if __name__=="__main__":
 completed=set()
 while len(completed)<len(tasks):
  ready=[name for name,deps in tasks.items() if name not in completed and set(deps)<=completed]
  print("Çalışabilir görevler:",ready);completed.update(ready)
