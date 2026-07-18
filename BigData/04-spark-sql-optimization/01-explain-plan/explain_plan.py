from __future__ import annotations
try:
 from pyspark.sql import SparkSession,functions as F
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[2]").appName("explain-plan").getOrCreate();df=spark.range(0,100).withColumn("group",F.col("id")%5);query=df.groupBy("group").count().filter("count > 10")
 query.explain("formatted");print("Planı okuyun: Exchange/shuffle, aggregate ve scan düğümlerini bulun.");spark.stop()
