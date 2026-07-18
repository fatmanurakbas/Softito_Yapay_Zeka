# LLM 02 — LLM Karşılaştırma Laboratuvarı

Bu proje, aday modelleri aynı Türkçe değerlendirme setinde karşılaştırır. Her model aynı sistem istemini, aynı kullanıcı girdisini ve aynı üretim ayarlarını alır; yanıt kalitesi, şema uygunluğu ve gecikme aynı sonuç dosyasında tutulur.

## Klasör yapısı

```text
02-llm-comparison/
├── configs/                    # Aday model ve üretim ayarları
├── data/evaluation_cases.json  # Sabit Türkçe görev seti
├── demo/                       # Canlı/dry-run karşılaştırma CLI'ı
├── evaluation/                 # Sonuç skorlama ve özet tablo
├── src/llm_comparison/         # İstemci ve skorlayıcı paket
├── reports/                    # Oluşturulan sonuç raporları
└── tests/
```

## Çalıştırma

Önce `configs/models.json` içindeki aday adlarını yerel modellerinizle değiştirin. `--dry-run` hiçbir model çağırmadan hangi deneylerin çalışacağını gösterir.

```bash
cd LLM/02-llm-comparison
python demo/run_comparison.py --dry-run
python demo/run_comparison.py --output reports/results.json
python evaluation/score_results.py --input reports/results.json
python -m unittest discover -s tests -v
```

## Karar ilkeleri

- Aynı model ailesinin farklı boyutlarını veya quant sürümlerini ayrı aday olarak kaydedin.
- Tek bir skorla karar vermeyin: görev başarısı, p95 gecikme, biçim uygunluğu, Türkçe akıcılık ve bellek/maliyet birlikte değerlendirilmelidir.
- Otomatik anahtar kelime skoru yalnızca hızlı regresyon kontrolüdür. Nihai seçimde hata örneklerini insan değerlendirmesiyle inceleyin.
