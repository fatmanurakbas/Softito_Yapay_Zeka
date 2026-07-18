# 02 — RNN ile Duygu Sınıflandırma

Bu çalışma, cümle tokenlarını embedding vektörlerine dönüştürür; RNN gizli durumunu kullanarak yorumun pozitif veya negatif olduğunu tahmin eder. Eğitim, BPTT ile NumPy üzerinden açıkça uygulanır.

```bash
python train_rnn.py
```

Veri küçük olduğu için sonuç eğitim mantığını gösterir, genelleme performansını değil. Gerçek projede veri setini eğitim/doğrulama/test olarak ayırın, mini-batch kullanın ve sabit bir baseline (TF-IDF + lojistik regresyon gibi) kurun.
