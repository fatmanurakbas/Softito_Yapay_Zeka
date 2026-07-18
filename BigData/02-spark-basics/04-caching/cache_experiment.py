"""Aynı RDD action'ını cache öncesi/sonrası ölçer."""
from __future__ import annotations
import time
try:
 from pyspark.sql import SparkSession
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[2]").appName("cache-experiment").getOrCreate();rdd=spark.sparkContext.parallelize(range(200000),4).map(lambda x:(x*x)%97)
 started=time.perf_counter();rdd.count();first=time.perf_counter()-started;rdd.cache();rdd.count();started=time.perf_counter();rdd.count();second=time.perf_counter()-started
 print(f"Cache öncesi: {first:.3f} sn | Cache sonrası: {second:.3f} sn");spark.stop()
