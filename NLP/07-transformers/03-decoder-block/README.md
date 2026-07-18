# 03 — Transformer Decoder Bloğu

Decoder, autoregressive üretim sırasında yalnızca geçmiş tokenlara bakmalıdır. Causal self-attention maskesi üst üçgeni kapatır; bu yüzden her satır yalnızca kendi konumuna ve öncesine attention verebilir.

```bash
python transformer_decoder.py
```

Betik, decoder çıktısını bir sözlük boyutuna projekte edip eğitim öncesi örnek next-token logits üretir.
