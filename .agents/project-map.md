# Proje Haritası

| Ana klasör | Odak | Tipik içerik |
|---|---|---|
| `MachineLearning` | Denetimli ve denetimsiz öğrenme | scikit-learn modelleri, karşılaştırmalar |
| `NLP` | Metin işleme ve dil modelleri | ön işleme, TF-IDF, RNN, Transformer |
| `LLM` | Büyük dil modeli uygulamaları | prompt, RAG, LoRA, değerlendirme |
| `SLM` | Yerel/küçük dil modelleri | Ollama, GGUF, Türkçe SLM |
| `DeepLearning` | Derin öğrenme temelleri | PyTorch, CNN, GRU, eğitim döngüleri |
| `BigData` | Dağıtık veri platformları | HDFS, Spark, Kafka, Airflow, Lakehouse |
| `WebScraping` | Sorumlu web verisi toplama | requests, Beautiful Soup, Playwright |
| `Docker` | Model servisleştirme | FastAPI, Compose, PostgreSQL |

## Yeni konu ekleme akışı

1. Hangi ana alana ait olduğunu belirleyin.
2. Sıralı numara ve kısa İngilizce klasör adı seçin.
3. README, örnek kod ve gerekirse `requirements.txt` ekleyin.
4. Örneği doğrulayın ve çalıştırma biçimini README'ye yazın.

## Mevcut Docker projeleri

- `Docker/ml_projem`: Tek FastAPI churn tahmin servisi.
- `Docker/ml-churn-platform`: Gateway ve üç model servisinden oluşan Compose platformu.
