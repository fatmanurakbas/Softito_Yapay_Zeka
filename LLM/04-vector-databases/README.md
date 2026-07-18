# LLM 04 — Vector Databases

Bu çalışma, vektör veritabanlarının temel kavramlarını küçük ve şeffaf bir yerel indeksle uygular: metni embedding'e dönüştürme, metadata ile saklama, cosine similarity ile arama ve filtreleme.

## Yapı

```text
04-vector-databases/
├── configs/                 # Embedding boyutu ve varsayılan arama ayarları
├── data/documents.json      # Örnek belge koleksiyonu
├── 01-embeddings/           # Deterministik hashing embedding demonstrasyonu
├── 02-vector-store/         # Kalıcı JSON vektör indeksi
├── 03-semantic-search/      # Similarity araması
├── 04-metadata-filtering/   # Filtreli arama
├── src/vector_store/        # Tekrar kullanılabilir paket
└── tests/
```

## Çalıştırma

```bash
cd LLM/04-vector-databases
python 01-embeddings/show_embedding.py --text "RAG belge getirir"
python 02-vector-store/build_index.py
python 03-semantic-search/search.py --query "yerel model belleği"
python 04-metadata-filtering/filter_search.py --query "model" --category slm
python -m unittest discover -s tests -v
```

Hashing embedding, kütüphane/donanım gerektirmeyen eğitim aracıdır; anlamsal kalite için üretimde uygun bir embedding modeli ve gerçek bir vektör veritabanı kullanın. Bu proje yine de upsert, metadata, indeks kalıcılığı ve top-k retrieval akışını doğrudan gösterir.
