# 01 — HTTP ve Beautiful Soup

Statik HTML sayfalarını indirmek için `requests`, HTML ağacını okumak için Beautiful Soup kullanılır. Bu yaklaşım, verinin ilk HTML yanıtında bulunduğu sayfalar için uygundur.

## Akış

1. URL'ye `GET` isteği gönderilir.
2. HTTP hata kodları `raise_for_status()` ile erken yakalanır.
3. HTML, `BeautifulSoup(..., "html.parser")` ile ayrıştırılır.
4. `title`, `a[href]`, sınıf veya etiket seçicileriyle veri alınır.

## Çalıştırma

```powershell
python fetch_page.py https://example.com
```

Örnek, sayfa başlığını ve bağlantı sayısını yazdırır. Kendi hedefinizde mutlaka izin, zaman aşımı (`timeout`) ve anlamlı bir User-Agent kullanın. Bir eleman her zaman bulunmayabileceği için `select_one` sonucunu `None` olasılığına karşı kontrol edin.
