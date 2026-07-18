# 02 — Transformer Encoder Bloğu

Encoder bloğu, çok başlıklı self-attention ve position-wise feed-forward katmanını residual bağlantılarla birleştirir. Layer normalization, katmanlar boyunca aktivasyonları dengeler.

```bash
python transformer_encoder.py
```

Bu eğitim örneği iki head kullanır ve yalnızca forward pass yapar; parametreler rastgele başlatıldığından çıktılar mimari akışı gösterir, anlamsal tahmin üretmez.
