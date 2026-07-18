# 01 — CLI ve Yerel Servis Kontrolü

Önce servis erişimini, ardından yerelde bulunan modelleri kontrol edin.

```bash
ollama --version
ollama list
python check_ollama.py
```

Betik, `/api/tags` uç noktasını çağırır ve her modelin adını, boyutunu ve quantization bilgisini yazdırır. Servis çalışmıyorsa bağlantı hatasını çözmek için Ollama uygulamasını başlatın.
