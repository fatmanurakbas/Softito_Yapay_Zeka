# 01 — Bag of Words

Bag of Words, belge içindeki kelimelerin sırasını yok sayar ve her kelimenin kaç kez geçtiğini vektör olarak kaydeder. Basit, hızlı ve doğrusal sınıflandırıcılar için güçlü bir başlangıç yaklaşımıdır.

```bash
python bow.py
```

Çıktıda sözlük ve her belgenin sayım vektörü yazdırılır. Kelime sırasını kaybettiği için `çok iyi` ile `iyi çok` aynı vektöre dönüşür; n-gramlar bu sınırlamayı azaltır.
