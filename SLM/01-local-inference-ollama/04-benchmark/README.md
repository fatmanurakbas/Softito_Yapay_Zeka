# 04 — Yerel Çıkarım Benchmark'ı

Benchmark betiği bir warm-up isteği yaptıktan sonra aynı promptu tekrarlı çalıştırır. Yanıtın `eval_count` ve `eval_duration` alanlarından token/saniye hesaplar; ayrıca toplam duvar saati süresini raporlar.

```bash
python benchmark.py --model <model-adı> --runs 3
```

Farklı model/quantization karşılaştırmalarında aynı promptu, context ayarını, warm-up politikasını ve donanımı koruyun.
