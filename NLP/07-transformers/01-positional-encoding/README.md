# 01 — Positional Encoding

Self-attention tek başına token sırasını bilmez. Sinüs ve kosinüs tabanlı positional encoding, her konuma özgü bir vektör üreterek bu bilgiyi token embedding'ine ekler.

```bash
python positional_encoding.py
```

Sabit sinüzoidal encoding eğitim gerektirmez; modern modellerde öğrenilebilir pozisyon embedding'leri veya RoPE gibi alternatifler de kullanılır.
