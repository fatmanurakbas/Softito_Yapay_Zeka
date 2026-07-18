# 01 — HDFS Temelleri

HDFS, büyük dosyaları bloklara bölerek birden fazla düğümde saklar. NameNode metadata'yı; DataNode'lar blokları tutar. Mevcut `../HDFS.ipynb` ile bu klasörü birlikte kullanın.

Çalışma hedefleri: dosya/blok/replikasyon kavramı, `hdfs dfs` komutları, küçük dosya problemi ve veri yerelliği.

## Egzersizler

```text
01-hdfs-fundamentals/
├── 01-cli-workflow/          # HDFS komut pratiği
├── 02-block-planning/        # Dosya/blok hesaplama
├── 03-replication-simulation/# DataNode replikasyon yerleşimi
├── 04-small-files/           # NameNode metadata maliyeti
└── tests/
```

```bash
python 02-block-planning/block_planner.py --file-mb 1024 --block-mb 128 --replication 3
python 03-replication-simulation/replication_simulator.py
python 04-small-files/small_files_impact.py --files 1000000 --metadata-bytes 200
```

Komut egzersizleri için çalışan bir HDFS ortamı gerekir; Python simülasyonları ise bağımsız çalışır.
