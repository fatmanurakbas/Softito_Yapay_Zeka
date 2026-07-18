# 05 — Uçtan Uca Ön İşleme Pipeline'ı

Bu betik normalleştirme, tokenization, stop word temizleme ve isteğe bağlı basit kök bulmayı tek bir tekrar kullanılabilir fonksiyonda birleştirir. Örnek metinler `../data/sample_texts.txt` dosyasından okunur.

```bash
python preprocessing_pipeline.py
```

`PreprocessingConfig` içindeki seçenekleri değiştirerek dönüşüm adımlarının çıktıya etkisini gözlemleyin.
