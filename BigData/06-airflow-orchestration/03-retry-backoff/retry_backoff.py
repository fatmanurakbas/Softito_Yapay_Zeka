from __future__ import annotations
from datetime import timedelta
def delays(retries:int,base_minutes:int)->list[timedelta]:return [timedelta(minutes=base_minutes*2**attempt) for attempt in range(retries)]
if __name__=="__main__":
 print("Retry gecikmeleri:",[str(value) for value in delays(3,5)]);print("Geçici hata için retry; kalıcı şema hatası için hızlı başarısızlık tercih edin.")
