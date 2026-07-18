# LLM 01 — Prompt Engineering Laboratuvarı

Bu proje, Türkçe LLM görevleri için tekrar kullanılabilir prompt şablonları oluşturur ve test eder. Zero-shot/few-shot yönlendirme, bağlam sınırı, yapılandırılmış JSON çıktı ve prompt regresyon kontrolü aynı çalışma altında toplanır.

## Klasör yapısı

```text
01-prompt-engineering/
├── configs/                    # Yerel model ve üretim ayarları
├── prompts/                    # Sürümleyebilen prompt şablonları
├── demo/                       # Prompt gösterimi ve canlı istek CLI'ı
├── evaluation/                 # JSON çıktı uygunluğu değerlendirmesi
├── src/prompt_lab/             # Şablon, şema ve Ollama istemcisi
├── tests/                      # Birim testleri
└── figures/                    # Deney sonuçları/grafikler
```

## Hızlı başlangıç

Önce `configs/app_config.json` içindeki `model` alanını yerel modelinizle değiştirin. Prompt'u model çağrısı yapmadan incelemek için `--offline` kullanın.

```bash
cd LLM/01-prompt-engineering
python demo/run_prompt.py --task summary --text "Uzun metniniz..." --offline
python demo/run_prompt.py --task sentiment --text "Ürün kaliteli fakat teslimat geç geldi."
python -m unittest discover -s tests -v
python evaluation/evaluate_structured_output.py --input evaluation/sample_outputs.json
```

## Prompt tasarım ilkeleri

- Rolü, görevi, girdi sınırını ve çıktı biçimini açıkça ayırın.
- Birkaç örnek (few-shot) yalnızca biçim veya karar mantığı gerçekten belirsiz olduğunda ekleyin.
- Şema kullanmak, JSON sözdizimini iyileştirir; alanların gerçekliğini garanti etmez.
- Prompt değişikliklerini sabit örnek seti üzerinde test edin. İyi görünen tek bir örnek, güvenilir bir iyileşme kanıtı değildir.
