# SLM 01 — Ollama ile Yerel Çıkarım

Bu çalışma, küçük dil modellerini Ollama üzerinden yerel makinede çalıştırmayı öğretir. Yerel API varsayılan olarak `http://localhost:11434/api` adresinde sunulur; model listeleme için `/tags`, sohbet için `/chat` uç noktaları kullanılır.

## Klasör yapısı

```text
01-local-inference-ollama/
├── 01-cli-basics/          # Kurulum kontrolü ve yerel model listesi
├── 02-local-chat/          # Python ile yerel chat isteği
├── 03-modelfile/           # Özel sistem istemli model şablonu
├── 04-benchmark/           # Gecikme ve token/saniye ölçümü
└── requirements.txt
```

## Başlangıç

1. Ollama'yı kurup arka plan servisinin çalıştığını doğrulayın.
2. İhtiyacınıza ve donanımınıza uygun bir modeli indirin: `ollama pull <model-adı>`.
3. `ollama run <model-adı>` ile komut satırında ilk isteği deneyin.
4. Aşağıdaki Python örneklerinde aynı model adını kullanın.

```bash
cd SLM/01-local-inference-ollama
python 01-cli-basics/check_ollama.py
python 02-local-chat/chat.py --model <model-adı> --prompt "Kısa bir Türkçe özet yaz."
python 04-benchmark/benchmark.py --model <model-adı>
```

## Önemli notlar

- Yerelde çalışmak verinin makinenizden çıkmamasına yardımcı olur; yine de loglar, model lisansı ve erişim yetkilerini ayrıca değerlendirin.
- İlk çağrı model yükleme süresi içerir. Benchmark'ta warm-up çağrısını gerçek ölçümden ayrı tutun.
- RAM/VRAM, context uzunluğu, quantization seviyesi ve model parametre sayısı birlikte gecikme ve kaliteyi belirler.
- Bu klasörün örnekleri `stream: false` kullanır; etkileşimli arayüzlerde streaming yanıtları ayrı ele alınmalıdır.
