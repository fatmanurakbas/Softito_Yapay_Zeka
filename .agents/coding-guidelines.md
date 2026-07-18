# İçerik ve Kodlama Kuralları

## Klasör düzeni

- Konular sıralı adlandırılır: `01-konu-adi`, `02-konu-adi`.
- Bir konu klasöründe en az `README.md` bulunur.
- Birden fazla uygulama varsa anlamlı alt klasörler kullanılır: `01-basics`, `02-pipeline`, `tests` gibi.
- Bağımlılıklar gerekli olduğunda klasöre `requirements.txt` eklenir.

## README standardı

Her README, kısa biçimde şu başlıkları içermelidir:

1. Konunun amacı ve ne öğrettiği
2. Klasör/dosya açıklaması
3. Kurulum veya çalıştırma komutu
4. Beklenen çıktı ya da önemli not

Konu kapsamı küçükse gereksiz teorik ayrıntı eklemeyin. Kullanıcı özellikle isterse daha detaylı anlatım eklenebilir.

## Python standardı

- Python 3.10+ ile uyumlu, okunabilir kod yazın.
- Fonksiyonları küçük tutun; giriş/çıkışları belirgin olsun.
- Sabit örnek verilerle, ağ erişimi olmadan çalışabilen demo tercih edin.
- Ağ, Docker, Spark, Ollama veya model indirme gerekiyorsa bunu README'de açıkça yazın.
- Gizli bilgi, token veya gerçek parola kod içine konulmaz.

## Doğrulama

- Uygun olduğunda `python -m unittest discover -s tests -v` kullanın.
- Test yoksa ilgili dosya için `python -m compileall -q .` ile sözdizimi kontrolü yapın.
- Bağımlılık eksikse paket kurmadan önce durumu belirtin; çalışma sonucunu buna göre raporlayın.

## Git hijyeni

- `.env`, anahtar, büyük geçici çıktı, cache ve yerel veritabanlarını eklemeyin.
- Var olan örnek veri ve model dosyalarını, kullanıcı istemedikçe silmeyin veya taşımayın.
- Oluşturulan çıktıları `outputs/`, `artifacts/` veya uygun bir `.gitignore` kuralıyla ayırın.
