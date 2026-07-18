from __future__ import annotations
try:
 from pyspark.sql import SparkSession,functions as F
 from pyspark.sql.window import Window
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[1]").appName("windows").getOrCreate();df=spark.createDataFrame([("u1",1,20),("u1",2,35),("u2",1,10),("u2",2,50)],"user string,day int,amount int");window=Window.partitionBy("user").orderBy("day")
 df.withColumn("previous",F.lag("amount").over(window)).withColumn("rank",F.rank().over(Window.partitionBy("user").orderBy(F.desc("amount")))).show();spark.stop()
