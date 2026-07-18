# 03 — Gradient Flow

RNN'de BPTT sırasında gradient, tekrar eden ağırlık matrisiyle zaman boyunca çarpılır. Norm çok küçükse vanishing gradient, çok büyükse exploding gradient oluşur.

```bash
python gradient_flow.py
```

Betik farklı tekrarlayan ağırlık ölçeklerinde gradient normlarının zaman adımıyla nasıl değiştiğini yazdırır.
