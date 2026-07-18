"""Olay kimliğiyle tekrar eden mesajları atlayan consumer örneği."""
from __future__ import annotations
def process(events):
 seen=set();processed=[]
 for event in events:
  if event["id"] in seen:continue
  seen.add(event["id"]);processed.append(event)
 return processed
if __name__=="__main__":
 events=[{"id":"e1","value":10},{"id":"e2","value":20},{"id":"e1","value":10}];print("İşlenen:",process(events));print("Üretimde seen set yerine kalıcı, atomik bir idempotency kaydı kullanın.")
