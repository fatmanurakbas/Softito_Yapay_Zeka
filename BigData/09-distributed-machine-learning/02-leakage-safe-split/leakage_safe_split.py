from __future__ import annotations
from datetime import date
rows=[{"id":"a","date":date(2025,1,1),"label":0},{"id":"b","date":date(2025,1,2),"label":1},{"id":"c","date":date(2025,1,3),"label":0}]
if __name__=="__main__":
 cutoff=date(2025,1,3);train=[row for row in rows if row["date"]<cutoff];test=[row for row in rows if row["date"]>=cutoff]
 print("Train ids:",[row["id"] for row in train]);print("Test ids:",[row["id"] for row in test]);print("Zaman bağımlı veride gelecek kayıtları train'e karıştırmayın.")
