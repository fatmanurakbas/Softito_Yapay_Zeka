from __future__ import annotations
from datetime import date,timedelta
if __name__=="__main__":
 start=date(2026,1,1);partitions=[start+timedelta(days=offset) for offset in range(7)]
 print("Örnek partition yolları:");[print(f"silver/events/date={day.isoformat()}/") for day in partitions]
 print("Yüksek kardinaliteli user_id gibi alanlarla partition açmak small-files sorununa yol açabilir.")
