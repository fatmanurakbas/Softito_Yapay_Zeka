# 04 — Spark SQL ve Optimizasyon

Sorgu planını `explain()` ile okuyun; shuffle, broadcast join, partition sayısı ve dosya boyutunun maliyetini ölçün.

Çalışma hedefleri: Catalyst planı, broadcast threshold, AQE ve yanlış cache kullanımını inceleme.

## Egzersizler

```text
04-spark-sql-optimization/
├── 01-explain-plan/         # explain() ile fiziksel plan
├── 02-partition-sizing/     # Hedef dosya boyutuna göre partition hesabı
├── 03-data-skew/            # Anahtar dağılımı ve skew oranı
├── 04-broadcast-join/       # Broadcast join planı
└── tests/
```

```bash
pip install -r requirements.txt
python 01-explain-plan/explain_plan.py
python 02-partition-sizing/partition_sizing.py --data-gb 500 --target-mb 256
python 03-data-skew/skew_analysis.py
python 04-broadcast-join/broadcast_join.py
```

Önce `explain()` çıktısını, ardından metrikleri inceleyin. Broadcast, küçük boyut tabloları için; repartition ise ancak dengesizlik veya çıktı dosyası boyutu problemi olduğunda kullanılmalıdır.
