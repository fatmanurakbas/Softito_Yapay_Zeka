from __future__ import annotations
def merge(target,source):
 index={row["id"]:row for row in target}
 for row in source:index[row["id"]]=row
 return list(index.values())
if __name__=="__main__":
 target=[{"id":"a","amount":10},{"id":"b","amount":20}];source=[{"id":"b","amount":25},{"id":"c","amount":5}]
 print("MERGE sonucu:",merge(target,source))
