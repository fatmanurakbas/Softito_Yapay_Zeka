# NLP 02 — Bag of Words ve TF-IDF

Bu çalışma, ön işlenmiş metinleri klasik makine öğrenmesi algoritmalarına girdi olabilecek sayısal vektörlere dönüştürür. Bag of Words (BoW) kelime sayımlarını; TF-IDF ise belgede ayırt edici olan kelimeleri ağırlıklandırır.

## Öğrenme hedefleri

- Sözlük (vocabulary) oluşturmak ve BoW vektörleri üretmek
- TF, IDF ve TF-IDF ağırlıklarını hesaplamak
- Unigram, bigram ve trigram kullanmak
- Cosine similarity ile belge araması yapmak
- Multinomial Naive Bayes ile küçük bir duygu sınıflandırması kurmak

## Klasör yapısı

```text
02-tfidf-bow/
├── 01-bag-of-words/              # Sayım tabanlı vektörleştirme
├── 02-tfidf/                     # TF-IDF vektörleştirme
├── 03-ngrams/                    # Unigram, bigram, trigram
├── 04-similarity-search/          # Cosine similarity ile arama
├── 05-text-classification/        # Multinomial Naive Bayes
├── data/reviews.csv              # Küçük etiketli Türkçe veri seti
├── figures/                      # Üretilecek grafikler
└── requirements.txt
```

## Çalıştırma

Örnekler Python 3.10+ ve standart kütüphane ile çalışır. Böylece vektörleştirmenin arkasındaki hesaplamalar açıkça görülebilir.

```bash
cd NLP/02-tfidf-bow
python 01-bag-of-words/bow.py
python 02-tfidf/tfidf.py
python 03-ngrams/ngrams.py
python 04-similarity-search/similarity_search.py
python 05-text-classification/naive_bayes_classifier.py
```

## Çalışma notları

- `data/reviews.csv` içindeki örnekleri artırın; küçük veri seti yalnızca öğrenme amaçlıdır.
- Test verisini model ve sözlük kurulduktan sonra kullanın; sözlük oluştururken test metinlerinden bilgi sızdırmayın.
- Duygu analizinde `değil` gibi olumsuzluk kelimelerini stop word olarak kaldırmayın.
- Sonraki klasör olan word embeddings, bu seyrek vektörlerin aksine kelimeleri yoğun ve anlamsal vektörlerle temsil eder.
