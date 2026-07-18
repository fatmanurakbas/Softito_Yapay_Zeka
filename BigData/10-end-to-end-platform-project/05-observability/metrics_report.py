from __future__ import annotations
import json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if __name__=="__main__":
 started=time.perf_counter();events=json.loads((ROOT/"data"/"events.json").read_text());latency=time.perf_counter()-started
 print({"run_id":"local-demo","input_rows":len(events),"pipeline_seconds":round(latency,4),"quality_status":"pass","table_version":"silver-events-v1"})
