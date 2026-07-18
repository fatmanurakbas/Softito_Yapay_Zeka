# 02 — TF-IDF

TF-IDF, bir belgede sık görünen fakat koleksiyonun tamamında nadir olan kelimelere daha yüksek ağırlık verir. Böylece `ve`, `ürün` gibi çok yaygın kelimelerin etkisi azalır.

```bash
python tfidf.py
```

Bu örnek, smooth IDF kullanır: `log((N + 1) / (df + 1)) + 1`. Sonuç vektörleri L2 normalize edilir; bu, cosine similarity için uygundur.
