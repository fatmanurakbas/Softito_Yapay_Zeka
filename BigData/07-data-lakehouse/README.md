# 07 — Data Lakehouse

Data lakehouse; nesne depolama, açık tablo biçimleri ve veri ambarı benzeri güvenilirlik özelliklerini birleştirir.

Çalışma hedefleri: bronze/silver/gold katmanları, medallion mimarisi, schema evolution ve veri yönetişimi.

## Egzersizler

```text
07-data-lakehouse/
├── 01-medallion-layers/     # Bronze → Silver → Gold dönüşümü
├── 02-schema-evolution/     # Uyumlu/uyumsuz şema değişimleri
├── 03-data-quality/         # Katmanlar arası kalite kuralları
├── 04-partition-design/     # Tarih tabanlı partition planı
└── tests/
```

```bash
python 01-medallion-layers/medallion_pipeline.py
python 02-schema-evolution/schema_evolution.py
python 03-data-quality/quality_rules.py
python 04-partition-design/partition_design.py
```

Bronze katmanı ham veriyi izlenebilir biçimde saklar; Silver temiz ve standartlaştırılmış veriyi; Gold ise iş tüketimi için toplulaştırılmış veriyi içerir. Her katmana veri kaynağı, şema sürümü ve kalite metriği eklemeyi alışkanlık hâline getirin.
