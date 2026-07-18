# LLM 03 — Retrieval-Augmented Generation (RAG)

Bu proje, bir LLM'in yalnızca model belleğine güvenmek yerine ilgili belgeleri getirerek yanıt üretmesini sağlar. Hattın her aşaması görünürdür: belge alma, chunk üretimi, retrieval, kaynaklı prompt ve retrieval değerlendirmesi.

## Klasör yapısı

```text
03-rag/
├── configs/                   # Yerel model ve retrieval ayarları
├── data/documents.json        # Örnek bilgi tabanı
├── 01-ingestion/              # Chunk üretimi
├── 02-retrieval/              # TF-IDF arama
├── 03-generation/             # Kaynaklı RAG yanıtı
├── 04-evaluation/             # Recall@k retrieval değerlendirmesi
├── src/rag_core/              # Tekrar kullanılabilir çekirdek paket
└── tests/
```

## Çalıştırma

```bash
cd LLM/03-rag
python 01-ingestion/build_chunks.py
python 02-retrieval/search.py --query "RAG halüsinasyonu nasıl azaltır?"
python 03-generation/rag_chat.py --question "Quantization neden kullanılır?" --offline
python 04-evaluation/evaluate_retrieval.py
python -m unittest discover -s tests -v
```

`--offline` yalnızca getirilen kaynakları ve üretim prompt'unu gösterir. Canlı yanıt için `configs/app_config.json` dosyasındaki model adını güncelleyin.

## Tasarım notları

- Bu öğrenme projesi şeffaflık için TF-IDF kullanır. Üretimde semantic embedding, metadata filtreleri ve reranking eklenebilir.
- Retrieval kalitesini üretimden ayrı ölçün; yanlış belge getiren bir sistemde LLM yanıtı iyi görünse bile güvenilir değildir.
- Yanıtta kullanılan chunk kimliklerini görünür tutmak, kaynak denetimi ve hata analizini kolaylaştırır.
