from __future__ import annotations
raw=[{"event_id":"e1","user":"Ada","amount":"120.5"},{"event_id":"e2","user":"Can","amount":"40"}]
def silver(rows):return [{"event_id":r["event_id"],"user":r["user"].lower(),"amount":float(r["amount"])} for r in rows]
def gold(rows):return {"revenue":sum(r["amount"] for r in rows),"orders":len(rows)}
if __name__=="__main__":
 clean=silver(raw);print("Bronze:",raw);print("Silver:",clean);print("Gold:",gold(clean))
