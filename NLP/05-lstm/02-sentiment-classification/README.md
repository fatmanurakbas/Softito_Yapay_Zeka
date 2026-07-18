# 02 — LSTM ile Duygu Sınıflandırma

Bu betik, Türkçe yorumları token dizisi olarak işler ve son gizli durumdan pozitif/negatif olasılığı üretir. Forward pass ve BPTT gradyanları NumPy ile açıkça yazılmıştır.

```bash
python train_lstm.py
```

Eğitim/test ayrımı sınıf dengesi korunarak yapılır. Küçük örnek veri yalnızca model akışını göstermek içindir; gerçek bir başarı ölçümü değildir.
