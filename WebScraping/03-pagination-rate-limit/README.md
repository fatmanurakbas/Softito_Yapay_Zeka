# 03 — Sayfalama ve Hız Sınırlama

Liste verileri çoğunlukla `?page=2`, `?offset=20` veya bir sonraki sayfa bağlantısı üzerinden sunulur. `pagination.py`, sayfa numarasını parametre olarak gönderip her yanıtı sırayla toplamanın en sade örneğini içerir.

## Neden bekleme gerekir?

Çok sık istek göndermek hem hedef servise yük olur hem de erişiminizin sınırlanmasına yol açabilir. Varsayılan bir saniyelik bekleme başlangıç için güvenli bir yaklaşımdır; sitenin açıkça belirttiği limit daha düşükse onu uygulayın.

## Geliştirme fikirleri

- Sonraki sayfa yoksa döngüyü durdurun.
- `429` ve geçici `5xx` yanıtlarında üstel geri çekilme kullanın.
- Tekrar çalışan işlerde aynı kaydı iki kez almamak için benzersiz kimlik saklayın.
- Büyük toplamlarda ilerlemeyi ve başarısız URL'leri loglayın.

Gerçek URL'yi ancak kullanım koşulları izin veriyorsa `collect_pages(url, page_count)` fonksiyonuna verin.
