# 03 — Stop Word Filtreleme

Stop word'ler, birçok belgede sık görülen ancak bazı görevlerde ayırt ediciliği düşük kelimelerdir. Bu adımda küçük ve düzenlenebilir bir Türkçe listeyle filtreleme yapılır.

```bash
python stopwords.py
```

`değil`, `asla` ve `çok` gibi kelimeler duygu/niyet analizinde anlam taşıyabilir. Bu nedenle listeyi veri setine ve hedef göreve göre doğrulayın.
