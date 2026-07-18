# Word2Vec — Skip-gram

Skip-gram, merkezdeki kelimeden çevresindeki bağlam kelimelerini tahmin eder. Bu betik eğitim sürecini görünür kılmak için negative sampling yerine tam softmax kullanır.

```bash
python word2vec_skipgram.py
```

Kod küçük derlem için tasarlanmıştır. Büyük veri üzerinde tam softmax pahalı olduğundan negative sampling veya hierarchical softmax kullanılır.
