# 05 — Dinamik Sayfalar

Bazı sayfalarda ilk HTML yalnızca uygulama kabuğunu içerir; ürünler veya tablolar JavaScript çalıştıktan sonra görünür. Bu durumda normal `requests` çağrısı yeterli olmayabilir. Playwright gerçek bir tarayıcı açarak DOM yüklendikten sonraki içeriğe erişir.

## Kurulum ve kullanım

```powershell
python -m pip install -r ..\requirements.txt
playwright install chromium
```

`playwright_example.py`, bir URL'ye gidip sayfanın başlığını döndüren en küçük örnektir. Gerçek projede `page.locator("...")` ile hedef öğeyi bekleyin; sabit `sleep` kullanmaktan kaçının.

Tarayıcı otomasyonu daha pahalıdır. Bu nedenle API veya statik HTTP seçeneği varsa önce onları değerlendirin. Oturum açma, CAPTCHA çözme veya erişim kontrolünü atlatma bu çalışmanın kapsamı dışındadır.
