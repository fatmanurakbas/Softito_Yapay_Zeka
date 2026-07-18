# 02 — Tokenization

Tokenization, metni modelin işleyebileceği cümle ve kelime birimlerine ayırır. Bu örnek, Türkçe karakterleri ve apostrofla ayrılmış ekleri koruyan hafif bir regex tabanlı tokenizer kullanır.

```bash
python tokenization.py
```

Regex yaklaşımı eğitim için şeffaftır. Üretimde alt kelime (subword) tabanlı Transformer tokenizer'ı, kullandığınız modelin tokenizer'ı olmalıdır.
