# NLP 03 — Word Embeddings

Bu çalışma, kelimeleri sayım vektörleri yerine anlam ve bağlam bilgisi taşıyan yoğun vektörler olarak temsil eder. Aynı bağlamlarda kullanılan kelimelerin vektörleri birbirine yaklaşır.

## Öğrenme hedefleri

- Word2Vec Skip-gram ile hedef–bağlam çiftlerinden embedding öğrenmek
- GloVe ile global birlikte-görünme (co-occurrence) bilgisini kullanmak
- FastText ile karakter n-gramlarının bilinmeyen kelimelere katkısını görmek
- Cosine similarity ile yakın kelimeleri incelemek

## Klasör yapısı

```text
03-word-embeddings/
├── word2vec/                 # Skip-gram ve softmax eğitimi
├── glove/                    # Birlikte-görünme matrisi ve GloVe kaybı
├── fasttext/                 # Karakter alt-kelimeleriyle Skip-gram
├── data/corpus.txt           # Küçük Türkçe eğitim derlemi
├── figures/                  # İsteğe bağlı projeksiyon/grafikler
└── requirements.txt
```

## Çalıştırma

```bash
cd NLP/03-word-embeddings
python word2vec/word2vec_skipgram.py
python glove/glove_cooccurrence.py
python fasttext/fasttext_subword.py
```

`numpy` gereklidir. Eğitim derlemi küçük tutulmuştur; bu nedenle sonuçlar yalnızca yöntemin işleyişini göstermek içindir. Gerçek projelerde büyük, alanınıza uygun derlem ve hazır/eğitilmiş embedding modelleri kullanın.

## TF-IDF'ten farkı

TF-IDF'te bir kelime, sözlükteki bir sütuna karşılık gelir; `iyi` ve `güzel` farklı ve bağımsızdır. Embedding yaklaşımı ise bağlamdan öğrenerek bu kelimeleri vektör uzayında yakınlaştırabilir.
