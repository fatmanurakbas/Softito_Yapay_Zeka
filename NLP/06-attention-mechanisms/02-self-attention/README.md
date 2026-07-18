# 02 — Self-Attention

Self-attention'da aynı dizi hem query, hem key, hem value üretir. Her token, dizideki diğer tokenlardan hangi bilgiyi alacağını öğrenir. Scaled dot-product skorları `sqrt(d_k)` ile ölçeklenir.

```bash
python self_attention.py
```

Betik ayrıca causal mask uygular. Bu maske, üretici (decoder) modellerde tokenın gelecekteki tokenları görmesini engeller.
