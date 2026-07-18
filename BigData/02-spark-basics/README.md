# 02 — Apache Spark Temelleri

Spark driver, executor, job, stage ve task ilişkisini öğrenin. RDD dönüşümleri lazy çalışır; action çağrıları işi başlatır.

Çalışma hedefleri: `SparkSession`, transformation/action farkı, partition ve cache/persist.

## Egzersizler

```text
02-spark-basics/
├── 01-rdd-word-count/       # map, flatMap, reduceByKey
├── 02-partition-planning/   # Partition dengesi simülasyonu
├── 03-lazy-evaluation/      # Lineage ve action etkisi
├── 04-caching/              # cache/persist ölçümü
└── tests/
```

```bash
pip install -r requirements.txt
python 01-rdd-word-count/rdd_word_count.py
python 02-partition-planning/partition_planner.py
python 03-lazy-evaluation/lazy_evaluation.py
python 04-caching/cache_experiment.py
```

Spark örnekleri yerel modda çalışır. Üretim cluster'ında partition sayısı, executor kaynakları ve veri skew'ü birlikte ele alınmalıdır.
