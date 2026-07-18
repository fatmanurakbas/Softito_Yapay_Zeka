"""RDD transformation ve action ile yerel word count örneği."""
from __future__ import annotations
try:
 from pyspark.sql import SparkSession
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[2]").appName("spark-basics-word-count").getOrCreate()
 lines=spark.sparkContext.parallelize(["spark hızlı veri işler","spark lazy evaluation kullanır","veri spark ile ölçeklenir"],2)
 counts=lines.flatMap(lambda line:line.lower().split()).map(lambda word:(word,1)).reduceByKey(lambda a,b:a+b)
 print("Partition sayısı:",lines.getNumPartitions());print("Word count:",sorted(counts.collect()));spark.stop()
