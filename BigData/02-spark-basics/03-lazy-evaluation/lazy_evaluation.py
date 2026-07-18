"""Transformation'ların action'a kadar çalışmadığını gösterir."""
from __future__ import annotations
try:
 from pyspark.sql import SparkSession
except ImportError as error: raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[1]").appName("lazy-evaluation").getOrCreate();rdd=spark.sparkContext.parallelize(range(8)).map(lambda x:x*2).filter(lambda x:x>6)
 print("Lineage (henüz action yok):\n",rdd.toDebugString().decode());print("Action sonucu:",rdd.collect());spark.stop()
