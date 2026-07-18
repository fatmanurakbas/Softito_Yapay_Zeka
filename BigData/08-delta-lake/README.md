# 08 — Delta Lake

Delta Lake, parquet tablolara transaction log üzerinden ACID işlemleri, time travel ve güvenilir upsert desteği ekler.

Çalışma hedefleri: `MERGE`, schema enforcement, version history, compaction ve küçük dosya yönetimi.

## Egzersizler

```text
08-delta-lake/
├── 01-transaction-log/      # Sürüm ve atomic commit simülasyonu
├── 02-merge-upsert/         # MERGE mantığı
├── 03-time-travel/          # Sürümden okuma
├── 04-compaction-planning/  # Small-files birleştirme planı
└── tests/
```

```bash
python 01-transaction-log/transaction_log.py
python 02-merge-upsert/merge_upsert.py
python 03-time-travel/time_travel.py
python 04-compaction-planning/compaction_plan.py
```

Gerçek Delta Lake ortamında `MERGE`, schema enforcement, version history ve `OPTIMIZE`/compaction işlemlerini üretim verisinde önce küçük bir tabloda test edin. Vacuum/retention ayarları time travel gereksinimiyle çelişmemelidir.
