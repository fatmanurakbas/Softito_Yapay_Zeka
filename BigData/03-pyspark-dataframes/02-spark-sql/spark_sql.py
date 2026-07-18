from __future__ import annotations
try:
 from pyspark.sql import SparkSession
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[1]").appName("spark-sql").getOrCreate();spark.createDataFrame([("TR",120),("TR",80),("DE",60)],"country string, amount int").createOrReplaceTempView("sales")
 spark.sql("SELECT country, SUM(amount) AS total FROM sales GROUP BY country ORDER BY total DESC").show();spark.stop()
