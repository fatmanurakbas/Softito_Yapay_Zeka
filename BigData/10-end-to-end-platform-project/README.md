# 10 — Uçtan Uca Veri Platformu Projesi

Kafka'dan olay alıp lakehouse katmanlarına yazan, Spark ile dönüştüren, Airflow ile orkestre eden ve izlenebilir metrikler üreten bir proje geliştirin.

Teslim ölçütleri: yeniden çalıştırılabilir altyapı, veri kalite testleri, idempotent pipeline, dokümantasyon, gecikme/maliyet metrikleri ve hata senaryoları.

## Proje yapısı

```text
10-end-to-end-platform-project/
├── data/events.json          # Kafka benzeri ham olaylar
├── 01-ingestion/             # Olay doğrulama ve idempotency
├── 02-lakehouse-transform/   # Bronze → Silver → Gold
├── 03-data-quality/          # Pipeline kalite kapısı
├── 04-orchestration/         # Airflow DAG taslağı
├── 05-observability/         # Gecikme ve kalite metrikleri
└── tests/
```

```bash
python 01-ingestion/ingest_events.py
python 02-lakehouse-transform/transform_events.py
python 03-data-quality/quality_gate.py
python 05-observability/metrics_report.py
```

Yerel örnek ham JSON kullanır. Üretimde ingestion Kafka'dan, dönüşüm Spark/Delta Lake'ten, orkestrasyon Airflow'dan ve metrikler bir izleme sisteminden gelmelidir. Her çalıştırma için `run_id`, kaynak offset aralığı, tablo sürümü ve kalite sonucu kaydedin.
