# 05 — Kafka ve Streaming

Kafka topic, partition, consumer group, offset ve delivery semantics kavramlarıyla olay akışını öğrenin.

Çalışma hedefleri: producer/consumer, anahtar seçimi, consumer lag, idempotent işleme ve Spark Structured Streaming entegrasyonu.

## Egzersizler

```text
05-kafka-streaming/
├── 01-topic-partitions/     # Anahtarın partition seçimine etkisi
├── 02-producer-consumer/    # Olay akışı ve offset simülasyonu
├── 03-consumer-groups/      # Partition atama dengesi
├── 04-idempotent-processing/# Tekrarlanan olayları güvenle işleme
└── tests/
```

```bash
python 01-topic-partitions/partition_by_key.py
python 02-producer-consumer/event_stream.py
python 03-consumer-groups/group_assignment.py
python 04-idempotent-processing/idempotent_consumer.py
```

Bu örnekler broker gerektirmeyen öğrenme simülasyonlarıdır. Gerçek Kafka ortamında topic retention, partition sayısı, replication factor, consumer lag ve şema uyumluluğunu ayrıca yönetin.
