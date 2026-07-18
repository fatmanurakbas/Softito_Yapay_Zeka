# FastText — Subword Embeddings

FastText, kelimeyi karakter n-gramlarına ayırır. Böylece `kitap`, `kitaplar` ve eğitimde hiç görülmeyen `kitaplık` kelimeleri ortak alt parçalar üzerinden ilişki kurabilir.

```bash
python fasttext_subword.py
```

Bu özellik Türkçe gibi eklemeli dillerde özellikle faydalıdır. Kod, eğitim için n-gram vektörlerinin ortalamasını merkez kelime vektörü olarak kullanır.
