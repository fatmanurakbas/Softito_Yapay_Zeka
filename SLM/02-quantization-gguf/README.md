# SLM 02 — Quantization ve GGUF

GGUF, GGML tabanlı çıkarım araçlarının model ağırlıklarını ve metadata bilgisini birlikte saklamak için kullandığı ikili dosya biçimidir. Quantization, yüksek hassasiyetli GGUF ağırlıklarını daha düşük hassasiyete dönüştürerek depolama ve bellek gereksinimini düşürür; bunun karşılığında kalite kaybı oluşabilir.

## Klasör yapısı

```text
02-quantization-gguf/
├── 01-gguf-inspection/      # Dosya boyutu ve adlandırma inceleme
├── 02-quantization/         # llama-quantize PowerShell iş akışı
├── 03-benchmark/            # llama-cli ile tekrar edilebilir ölçüm
├── 04-comparison/           # Benchmark CSV sonuçlarını sıralama
├── models/                  # GGUF modelleri (Git'e eklenmez)
└── results/                 # Benchmark çıktıları
```

## Çalışma sırası

1. Yüksek hassasiyetli bir kaynak GGUF hazırlayın veya edinin.
2. `llama-quantize` ile hedef quant türünde yeni GGUF üretin.
3. Aynı prompt, context ve token limitiyle her modeli benchmark edin.
4. Boyut, token/saniye, bellek ve görev kalitesini birlikte karşılaştırın.

```powershell
cd SLM/02-quantization-gguf
python 01-gguf-inspection/inspect_gguf.py --models-dir models
.\02-quantization\quantize.ps1 -Source models\source-f16.gguf -Output models\model-q4_k_m.gguf -Type Q4_K_M
python 03-benchmark/benchmark_gguf.py --model models\model-q4_k_m.gguf
python 04-comparison/compare_results.py --input results\benchmarks.csv
```

## Doğru değerlendirme

- Aynı model ailesinin aynı sürümünü karşılaştırın; yalnızca quant türünü değiştirin.
- İlk çağrıyı warm-up kabul edin. Model yükleme süresini üretim hızından ayrı raporlayın.
- Bir quant türünün kalitesini yalnızca dosya boyutuyla değerlendirmeyin: Türkçe görev örnekleri, halüsinasyon ve biçim uyumu için de test edin.
- Re-quantization yerine mümkünse yüksek hassasiyetli özgün kaynak GGUF'tan başlayın.

`llama.cpp` akışında model önce GGUF'a dönüştürülür, ardından `llama-quantize` ile quantize edilir. Bu klasördeki otomasyon da bu sırayı varsayar.
