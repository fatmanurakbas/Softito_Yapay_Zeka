from __future__ import annotations
table=[];history=[]
def commit(rows,operation):
 global table
 table=rows;history.append({"version":len(history),"operation":operation,"rows":len(rows)})
if __name__=="__main__":
 commit([{"id":"a","amount":10}],"WRITE");commit(table+[{"id":"b","amount":20}],"APPEND");print("Geçmiş:",history);print("Güncel tablo:",table)
