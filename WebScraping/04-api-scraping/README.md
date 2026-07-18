# 04 — API'den Veri Çekme

Bir platform resmi ve belgelenmiş bir API sunuyorsa ilk tercih odur. API yanıtları yapılandırılmış JSON olduğundan HTML seçicilerinin kırılmasına daha az açıktır; sayfalama, kimlik doğrulama ve kota bilgileri de genellikle açıkça belgelenir.

## Örnek akış

`api_client.py` içinde `fetch_json` fonksiyonu isteği gönderir, HTTP hatalarını kontrol eder ve JSON'u Python `dict` veya `list` olarak döndürür.

```python
items = fetch_json("https://izinli-api.example/items")
```

API anahtarlarını kod içine yazmayın. Ortam değişkeni veya yerel `.env` dosyası kullanın; `.env` dosyasının Git'e eklenmediğinden emin olun. Kimlik doğrulama yöntemi, kota ve yeniden deneme davranışı için ilgili API belgelerini esas alın.
