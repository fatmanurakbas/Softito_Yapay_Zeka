# 04 — TF-IDF ile Benzerlik Araması

Bu örnek, sorguyu ve belgeleri TF-IDF vektörlerine çevirir; sonra cosine similarity ile en yakın belgeleri sıralar. Bu yaklaşım bilgi erişimi ve basit öneri sistemleri için temel oluşturur.

```bash
python similarity_search.py
```

TF-IDF yalnızca sözcüksel eşleşmeyi yakalar. Eş anlamlıları ve anlamsal yakınlığı daha iyi yakalamak için sonraki aşamada embedding tabanlı arama kullanılır.
