# 06 — Temizleme ve Dışa Aktarma

Webden gelen metinler boşluk, eksik alan veya farklı sayı biçimleri içerebilir. Analizden önce ham veri ile temizlenmiş veri ayrılmalı; dönüşüm kuralları açıkça tanımlanmalıdır.

`clean_export.py` örneği:

- `title` alanının baş/son boşluklarını temizler,
- başlığı veya fiyatı olmayan kayıtları eler,
- fiyatı `float` değerine dönüştürür,
- sonucu UTF-8 CSV olarak yazar.

```python
rows = clean(raw_rows)
save_csv(rows, "products.csv")
```

Gerçek bir veri setinde tarihleri ISO-8601 biçimine dönüştürün, para birimini ayrı alan olarak saklayın ve dönüşemeyen kayıtları sessizce kaybetmek yerine hata tablosuna/loga yazın. Çıktı CSV dosyaları `.gitignore` ile kaynak koddan ayrı tutulur.
