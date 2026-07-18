# 03 — GGUF Benchmark

Bu betik `llama-cli` komutunu bir warm-up çağrısından sonra tekrarlı çalıştırır ve dışarıdan ölçülen duvar saati süresini CSV'ye kaydeder. Aynı prompt ve token sayısını koruyarak quant sürümlerini karşılaştırın.

```bash
python benchmark_gguf.py --model ../models/model-q4_k_m.gguf --cli C:\tools\llama-cli.exe --runs 3
```

Duvar saati ölçümü yükleme, prompt işleme ve üretimi kapsar. Ayrıntılı token/saniye ölçümü için llama.cpp'nin kendi benchmark aracını da aynı donanımda çalıştırabilirsiniz.
