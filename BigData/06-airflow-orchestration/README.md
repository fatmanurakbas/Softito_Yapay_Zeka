# 06 — Airflow ve DAG Orkestrasyonu

Airflow görev bağımlılıklarını, yeniden deneme politikasını ve schedule/backfill davranışını yönetir. Mevcut `../Airflow.ipynb` ve `../DAG.ipynb` bu başlığın başlangıç materyalidir.

Çalışma hedefleri: DAG tasarımı, task idempotency, XCom sınırları, retry/alert ve veri kalitesi kontrolleri.

## Egzersizler

```text
06-airflow-orchestration/
├── 01-taskflow-dag/         # TaskFlow API ile günlük DAG
├── 02-dependencies/         # Bağımlılık grafiği simülasyonu
├── 03-retry-backoff/        # Retry zamanlaması
├── 04-data-quality-gate/    # Pipeline öncesi kalite kontrolü
└── tests/
```

```bash
python 02-dependencies/dependency_graph.py
python 03-retry-backoff/retry_backoff.py
python 04-data-quality-gate/data_quality_gate.py
```

Airflow DAG'ını çalıştırmak için `01-taskflow-dag/daily_sales_dag.py` dosyasını Airflow `dags/` dizinine kopyalayın. Görevler idempotent olmalı; aynı logical date için tekrar çalıştığında yinelenen veri üretmemelidir.
