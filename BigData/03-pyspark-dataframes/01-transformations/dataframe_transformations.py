from __future__ import annotations
try:
 from pyspark.sql import SparkSession,functions as F
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[2]").appName("df-transformations").getOrCreate();df=spark.createDataFrame([(1,"elektronik",100.0),(2,"kitap",40.0),(3,"elektronik",None)],"id int, category string, price double")
 result=df.fillna({"price":0.0}).withColumn("taxed_price",F.round(F.col("price")*1.2,2)).groupBy("category").agg(F.count("*").alias("count"),F.sum("taxed_price").alias("revenue"));result.show();spark.stop()
