from __future__ import annotations
try:
 from pyspark.sql import SparkSession
 from pyspark.ml import Pipeline
 from pyspark.ml.feature import VectorAssembler
 from pyspark.ml.classification import LogisticRegression
except ImportError as error:raise SystemExit("Önce `pip install -r requirements.txt` çalıştırın.") from error
if __name__=="__main__":
 spark=SparkSession.builder.master("local[2]").appName("spark-ml").getOrCreate();df=spark.createDataFrame([(0.,0.,0.),(0.,1.,1.),(1.,0.,1.),(1.,1.,1.)],"x1 double,x2 double,label double")
 pipeline=Pipeline(stages=[VectorAssembler(inputCols=["x1","x2"],outputCol="features"),LogisticRegression(maxIter=20)])
 model=pipeline.fit(df);model.transform(df).select("x1","x2","label","prediction","probability").show();spark.stop()
