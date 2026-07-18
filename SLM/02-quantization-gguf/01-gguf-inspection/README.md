# 01 — GGUF Dosyalarını İnceleme

Bu betik model klasöründeki `.gguf` dosyalarını listeler, dosya boyutunu gösterir ve dosya adındaki yaygın quant etiketini (`Q4_K_M`, `Q8_0` gibi) ayıklar.

```bash
python inspect_gguf.py --models-dir ../models
```

Dosya adı güvenilir metadata yerine geçmez; gerçek quant türünü doğrulamak için model sağlayıcısının kartını veya ilgili çıkarım aracının metadata çıktısını kontrol edin.
