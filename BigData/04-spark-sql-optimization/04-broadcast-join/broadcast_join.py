from __future__ import annotations
try:
 from pyspark.sql import SparkSession,functions as F
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[2]").appName("broadcast-join").getOrCreate();fact=spark.range(1000).withColumn("key",F.col("id")%10);dimension=spark.createDataFrame([(i,f"kategori-{i}") for i in range(10)],"key long,name string")
 fact.join(F.broadcast(dimension),"key").explain();print("Physical plan içinde BroadcastHashJoin arayın.");spark.stop()
