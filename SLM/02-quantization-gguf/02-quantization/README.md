# 02 — `llama-quantize` ile Quantization

PowerShell betiği kaynak GGUF, hedef GGUF ve quant türünü açık parametrelerle alır. Betik kaynak dosyanın varlığını ve hedef klasörü kontrol eder; ardından `llama-quantize input output type` komutunu çalıştırır.

```powershell
.\quantize.ps1 -Source ..\models\source-f16.gguf -Output ..\models\model-q4_k_m.gguf -Type Q4_K_M -LlamaQuantizePath C:\tools\llama-quantize.exe
```

`llama-quantize` yürütülebilir dosyasını llama.cpp derlemenizden sağlamalısınız. Yeni quant denemelerinde kaynak olarak daha önce quantize edilmiş bir dosya değil, yüksek hassasiyetli sürüm kullanın.
