from __future__ import annotations
def quality_report(rows):
 return {"row_count":len(rows),"null_user":sum(not row.get("user") for row in rows),"negative_amount":sum(row.get("amount",0)<0 for row in rows),"unique_event_ids":len({row.get("event_id") for row in rows})}
if __name__=="__main__":
 rows=[{"event_id":"e1","user":"ada","amount":10},{"event_id":"e2","user":None,"amount":-1}];print(quality_report(rows))
