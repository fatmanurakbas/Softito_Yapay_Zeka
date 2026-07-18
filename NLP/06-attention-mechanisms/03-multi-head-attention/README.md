# 03 — Multi-Head Attention

Tek bir attention işlemi tek tür ilişkiye odaklanabilir. Multi-head attention, farklı projeksiyonlarla birden fazla attention head çalıştırır; sonra sonuçları birleştirir. Bu, sözdizimsel ve anlamsal ilişkilerin paralel öğrenilmesini sağlar.

```bash
python multi_head_attention.py
```

Gerçek Transformer katmanlarında birleştirilmiş çıktı ayrıca bir çıktı projeksiyonundan geçirilir ve residual bağlantı/normalization ile kullanılır.
