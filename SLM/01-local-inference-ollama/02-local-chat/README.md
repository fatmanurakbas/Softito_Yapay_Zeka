# 02 — Yerel Chat API

Bu betik Ollama'nın `/api/chat` uç noktasına mesaj dizisi gönderir. `stream: false` sayesinde yanıt tek JSON nesnesi olarak gelir; modelin yanıtı ile süre/token ölçüleri birlikte yazdırılır.

```bash
python chat.py --model <model-adı> --prompt "RAG nedir? İki cümleyle açıkla."
```

`--system` seçeneği sistem mesajı ekler. Model adının `ollama list` çıktısındaki yerel bir ad olması gerekir.
