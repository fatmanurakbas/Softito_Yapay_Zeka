# Web Scraping

Bu bölüm, web üzerindeki **izinli ve herkese açık** veriyi programatik olarak toplama, ayıklama ve saklama pratiği içindir. Amaç bir web sitesini yoğun isteklerle taramak değil; küçük, tekrarlanabilir ve sorumlu veri alma akışları kurmaktır.

## Öğrenme yolu

| Bölüm | Konu | Çıktı |
|---|---|---|
| 01 | HTTP ve Beautiful Soup | HTML içinden başlık ve bağlantı ayıklama |
| 02 | CSS/XPath seçicileri | Hedef elemanı doğru seçme |
| 03 | Sayfalama ve hız sınırlama | Birden çok sayfayı kontrollü toplama |
| 04 | API'den veri çekme | JSON yanıtını kullanma |
| 05 | Dinamik sayfalar | JavaScript içerikleri için Playwright |
| 06 | Temizleme ve dışa aktarma | Normalize edilmiş CSV üretme |
| 07 | Etik, robots.txt ve dayanıklılık | İzin, hata ve sınır yönetimi |

## Kurulum

```powershell
cd WebScraping
python -m pip install -r requirements.txt
```

Dinamik tarayıcı örneği için Playwright tarayıcısını da kurun:

```powershell
playwright install chromium
```

## Önerilen çalışma sırası

Önce `01` ve `02` içindeki statik HTML örnekleriyle seçici yazın. Ardından `03` ile sayfalama/hız sınırını, `04` ile API tercihini öğrenin. Gerekliyse en son `05` içindeki tarayıcı otomasyonuna geçin. Toplanan veriyi `06` ile temizleyip `07` ilkelerine göre çalıştığınızı kontrol edin.

## Sorumlu kullanım kontrol listesi

- Site kullanım koşullarını ve `robots.txt` kurallarını okuyun.
- API varsa öncelikle API'yi kullanın.
- Kişisel veri, oturum gerektiren sayfa veya erişim engelini aşmaya yönelik veri toplamayın.
- Açık bir User-Agent gönderin; istekleri yavaşlatın ve hatalarda geri çekilin.
- Ham veriyi, çalışma zamanı ve kaynak URL bilgisini kayıt altında tutun.
