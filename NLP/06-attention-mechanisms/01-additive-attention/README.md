# 01 — Additive Attention

Bahdanau attention, decoder'ın mevcut gizli durumu ile encoder'ın her gizli durumunu küçük bir sinir ağı içinde karşılaştırır. Uyum skorları softmax'ten geçirilir ve ağırlıklı encoder özeti (context vector) üretilir.

```bash
python additive_attention.py
```

Bu yaklaşım, sabit boyutlu tek bir encoder vektörünün uzun dizilerde yarattığı bilgi darboğazını azaltır.
