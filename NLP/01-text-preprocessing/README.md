# NLP 01 — Metin Ön İşleme

Bu çalışma, ham Türkçe metni makine öğrenmesi ve NLP modellerinin kullanabileceği temiz token dizilerine dönüştürür. Her alt klasör tek bir tekniği izole biçimde gösterir; `05-pipeline` ise bunları uçtan uca bir akışta birleştirir.

## Öğrenme hedefleri

- Metni Unicode, büyük/küçük harf, URL, e-posta ve noktalama açısından normalleştirmek
- Cümle ve kelime tokenization uygulamak
- Stop word temizliğinin bilgi kaybı riskini anlamak
- Türkçedeki eklemeli yapıyı basit kök bulma yaklaşımıyla incelemek
- Dönüşümlerin sınıflandırma veya arama görevine etkisini gözlemlemek

## Klasör yapısı

```text
01-text-preprocessing/
├── 01-text-normalization/        # Temizleme ve normalleştirme
├── 02-tokenization/              # Cümle/kelime tokenization
├── 03-stopwords/                 # Stop word filtreleme
├── 04-stemming-lemmatization/    # Basit Türkçe kök bulma
├── 05-pipeline/                  # Uçtan uca ön işleme akışı
├── data/sample_texts.txt         # Deneme metinleri
├── figures/                      # Üretilecek görseller
├── requirements.txt
└── .gitignore
```

## Başlangıç

Python 3.10+ yeterlidir; örnekler yalnızca standart kütüphane kullanır.

```bash
cd NLP/01-text-preprocessing
python 01-text-normalization/normalization.py
python 02-tokenization/tokenization.py
python 03-stopwords/stopwords.py
python 04-stemming-lemmatization/stemming_lemmatization.py
python 05-pipeline/preprocessing_pipeline.py
```

## Önerilen çalışma sırası

1. Her betiği tek tek çalıştırın ve çıktıdaki dönüşümleri inceleyin.
2. `data/sample_texts.txt` dosyasına kendi Türkçe örneklerinizi ekleyin.
3. Pipeline ayarlarında stop word ve kök bulmayı açıp kapatarak çıktıları karşılaştırın.
4. Sonraki aşamada bu tokenları TF-IDF/Bag of Words özelliklerine dönüştürebilirsiniz.

> Not: Ön işleme göreve bağlıdır. Örneğin duygu analizinde `değil` gibi olumsuzluk belirten kelimeleri stop word olarak silmek model kalitesini düşürebilir.
