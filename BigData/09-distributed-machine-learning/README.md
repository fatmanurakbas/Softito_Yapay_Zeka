# 09 — Dağıtık Makine Öğrenmesi

Veri hazırlama ve model eğitimini cluster maliyeti, veri sızıntısı ve deney tekrarlanabilirliği ile birlikte ele alın.

Çalışma hedefleri: Spark ML pipeline, feature store kavramı, batch inference, model registry ve eğitim/servis ayrımı.

## Egzersizler

```text
09-distributed-machine-learning/
├── 01-spark-ml-pipeline/    # Feature assembler + logistic regression
├── 02-leakage-safe-split/   # Zaman/grup bazlı bölme ilkeleri
├── 03-batch-inference/      # Toplu skor üretimi
├── 04-model-registry/       # Model sürümü ve promotion akışı
└── tests/
```

```bash
pip install -r requirements.txt
python 01-spark-ml-pipeline/spark_ml_pipeline.py
python 02-leakage-safe-split/leakage_safe_split.py
python 03-batch-inference/batch_inference.py
python 04-model-registry/model_registry.py
```

Dağıtık eğitimde hedef değişken, feature hesaplama tarihi ve veri bölmesi birlikte izlenmelidir. Batch inference çıktısına model sürümü, feature sürümü ve skor tarihi ekleyin.
