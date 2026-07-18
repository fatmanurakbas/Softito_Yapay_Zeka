from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def deduplicate(events):
 seen=set();return [event for event in events if not (event["event_id"] in seen or seen.add(event["event_id"]))]
if __name__=="__main__":
 events=json.loads((ROOT/"data"/"events.json").read_text());accepted=deduplicate(events);print(f"Ingestion: {len(events)} ham olay -> {len(accepted)} benzersiz olay")
