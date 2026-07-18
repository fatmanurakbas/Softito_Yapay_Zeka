# LLM 08 — Quantization

Bu proje, Transformers/bitsandbytes ile 4-bit ve 8-bit model yüklemeyi, bellek tahminini ve aynı promptlarda kalite–gecikme karşılaştırmasını kapsar.

```text
08-quantization/
├── configs/                 # Model ve quant ayarları
├── data/prompts.json        # Sabit karşılaştırma promptları
├── 01-memory-estimation/    # Teorik ağırlık belleği
├── 02-load-quantized/       # BitsAndBytesConfig ile yükleme
├── 03-comparison/           # Yanıt/latency sonuç kaydı
└── tests/
```

```bash
cd LLM/08-quantization
pip install -r requirements.txt
python 01-memory-estimation/estimate_memory.py --parameters-billions 7
python 02-load-quantized/load_model.py --mode 4bit
python 03-comparison/compare.py --mode 8bit
```

`configs/quant_config.json` içindeki temel model adını değiştirin. Quantization kaliteyi garanti etmez; aynı model, aynı prompt seti ve aynı donanımda ölçüm yapın. 4-bit eğitim yalnızca ek parametrelerin (ör. LoRA) eğitimi için uygundur.
