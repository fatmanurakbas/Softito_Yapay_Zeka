# 07 — Etik, robots.txt ve Dayanıklılık

Teknik olarak erişilebilir olması, verinin otomatik toplanmasının her zaman uygun olduğu anlamına gelmez. Toplama işi başlamadan önce hedef sitenin kullanım koşullarını, telif/lisans durumunu, gizlilik beklentisini ve `robots.txt` yönergelerini değerlendirin.

## Uygulanacak ilkeler

- Kişisel, hassas veya oturum arkasındaki verileri toplamayın.
- `robots.txt` izni yoksa ya da koşullar yasaklıyorsa işlem yapmayın.
- Kim olduğunuzu belirten bir User-Agent kullanın; yüksek paralellik ve agresif tekrar denemelerinden kaçının.
- Bağlantı, zaman aşımı ve `429` hatalarını kayıt altına alın; sınırlama gelirse işi durdurun veya yavaşlatın.
- Kaynak URL, toplama zamanı ve dönüşüm sürümünü saklayarak verinin izlenebilirliğini sağlayın.

`request_policy.py`, `RobotFileParser` ile bir hedef URL'nin erişilebilir olup olmadığını kontrol etmenin temel örneğini verir. Bu kontrol tek başına hukuki veya sözleşmesel izin yerine geçmez; kullanım koşulları ayrıca incelenmelidir.
