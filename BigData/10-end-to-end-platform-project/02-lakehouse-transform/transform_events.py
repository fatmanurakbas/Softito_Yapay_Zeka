from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def transform(events):
 silver=[{**event,"amount":float(event["amount"]),"event_type":event["event_type"].lower()} for event in events]
 gold={"purchase_count":sum(event["event_type"]=="purchase" for event in silver),"revenue":sum(event["amount"] for event in silver)}
 return silver,gold
if __name__=="__main__":
 silver,gold=transform(json.loads((ROOT/"data"/"events.json").read_text()));print("Silver satır:",len(silver));print("Gold metrik:",gold)
