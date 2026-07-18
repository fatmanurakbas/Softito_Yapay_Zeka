from __future__ import annotations
def compatible(old:set[str],new:set[str])->bool:return old<=new
if __name__=="__main__":
 current={"event_id","user","amount"};additive={"event_id","user","amount","currency"};breaking={"event_id","user"}
 print("Additive değişim uyumlu mu?",compatible(current,additive));print("Alan kaldırma uyumlu mu?",compatible(current,breaking))
