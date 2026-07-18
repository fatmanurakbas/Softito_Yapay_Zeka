# Türkçe SLM Asistanı

Bu proje, yerelde çalışan küçük bir dil modelini Türkçe soru-cevap ve kısa özetleme işleri için yapılandırılmış bir asistana dönüştürür. Görseldeki proje düzeni temel alınmış; buna ek olarak yapılandırma doğrulama, bağlamlı istem üretimi, Ollama istemcisi ve birim testleri eklenmiştir.

## Klasör yapısı

```text
turkce-slm/
├── checkpoints/              # Yerel adapter/checkpoint notları; ağırlıklar Git dışı
├── configs/                  # Uygulama yapılandırması
├── demo/                     # Komut satırı demosu ve örnek sorular
├── figures/                  # Değerlendirme/grafik çıktıları
├── src/turkce_slm/           # Uygulama paketi
├── tests/                    # Standart kütüphane birim testleri
└── requirements.txt
```

## Hızlı başlangıç

1. Yerel Ollama kurulumunuzda bir model indirin: `ollama pull <model-adı>`.
2. [app_config.json](configs/app_config.json) içindeki `model` alanını yerel model adınızla değiştirin.
3. Demo çalıştırın:

```bash
cd SLM/turkce-slm
python demo/run_demo.py --question "Yapay zekâ nedir?"
python demo/run_demo.py --question "Metni iki maddede özetle" --context "...metniniz..."
python -m unittest discover -s tests -v
```

## Uygulama davranışı

- Türkçe karakterlerin `İ/I` dönüşümünü gözeten hafif metin normalleştirme uygulanır.
- Sistem istemi kısa, açık ve belirsizlikte dürüst yanıt vermeye yöneliktir.
- Bağlam verildiğinde modelden yalnızca bu bağlama dayanması istenir; bağlamda yanıt yoksa bunu belirtmesi beklenir.
- Ollama isteği `stream: false` ile gönderilir; yanıt ve süre/token metrikleri tek sonuçta alınır.

## Sonraki geliştirmeler

- Temsilî Türkçe test seti ve insan değerlendirmesi ekleyin.
- Prompt sürümünü, model adını ve quant türünü benchmark sonuçlarıyla beraber kaydedin.
- Alan verisi için RAG veya LoRA uyarlamasını ancak güçlü bir baseline sonrasında değerlendirin.
