from __future__ import annotations
def validate(rows:list[dict])->list[str]:
 errors=[]
 if not rows:errors.append("Kaynak veri boş.")
 if any(row.get("amount",0)<0 for row in rows):errors.append("Negatif amount bulundu.")
 if len({row.get("id") for row in rows})!=len(rows):errors.append("Tekrarlanan id bulundu.")
 return errors
if __name__=="__main__":
 sample=[{"id":"a","amount":10},{"id":"b","amount":20}];errors=validate(sample);print("QUALITY PASS" if not errors else errors)
