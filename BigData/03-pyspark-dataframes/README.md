# 03 — PySpark DataFrames

Dağıtık tablosal veri işlemede schema, `select`, `filter`, `groupBy`, `join` ve window fonksiyonlarını çalışın.

Çalışma hedefleri: şema doğrulama, null yönetimi, partitioned parquet yazma ve skew gözlemi.

## Egzersizler

```text
03-pyspark-dataframes/
├── 01-transformations/      # select, filter, withColumn, groupBy
├── 02-spark-sql/            # Temp view ve SQL sorguları
├── 03-joins/                # Join türleri ve broadcast ipucu
├── 04-window-functions/     # rank, lag ve partitionBy
└── tests/
```

```bash
pip install -r requirements.txt
python 01-transformations/dataframe_transformations.py
python 02-spark-sql/spark_sql.py
python 03-joins/joins.py
python 04-window-functions/window_functions.py
```

Gerçek projelerde şemayı açık tanımlayın, null oranını ölçün, join öncesinde veri hacmini kontrol edin ve partition sayısını dosya boyutuyla birlikte değerlendirin.
