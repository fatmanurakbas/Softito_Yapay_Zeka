from __future__ import annotations
try:
 from pyspark.sql import SparkSession,functions as F
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[2]").appName("joins").getOrCreate();orders=spark.createDataFrame([(1,"u1",90),(2,"u2",40),(3,"u3",20)],"order_id int,user_id string,amount int");users=spark.createDataFrame([("u1","Ada"),("u2","Can")],"user_id string,name string")
 orders.join(F.broadcast(users),"user_id","left").show();print("Broadcast yalnızca gerçekten küçük boyutlu boyut tablolarında kullanılmalıdır.");spark.stop()
