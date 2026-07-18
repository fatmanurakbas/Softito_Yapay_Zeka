from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def checks(events):
 return {"unique_event_ids":len({e["event_id"] for e in events})==len(events),"non_negative_amount":all(e["amount"]>=0 for e in events),"valid_event_type":all(e["event_type"] in {"view","purchase"} for e in events)}
if __name__=="__main__":
 results=checks(json.loads((ROOT/"data"/"events.json").read_text()));print(results);print("QUALITY PASS" if all(results.values()) else "QUALITY FAIL")
