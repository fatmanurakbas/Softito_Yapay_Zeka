# NLP 06 — Attention Mekanizmaları

Attention, modelin bir çıktı üretirken girdinin her parçasına aynı önemle bakmak yerine ilgili tokenlara ağırlık vermesini sağlar. Bu çalışma encoder–decoder attention'dan Transformer'lardaki self-attention'a doğru ilerler.

## Klasör yapısı

```text
06-attention-mechanisms/
├── 01-additive-attention/       # Bahdanau tipi encoder–decoder attention
├── 02-self-attention/           # Scaled dot-product ve causal mask
├── 03-multi-head-attention/     # Birden çok attention head'i
├── figures/                     # İsteğe bağlı attention haritaları
└── requirements.txt
```

## Çalıştırma

```bash
cd NLP/06-attention-mechanisms
python 01-additive-attention/additive_attention.py
python 02-self-attention/self_attention.py
python 03-multi-head-attention/multi_head_attention.py
```

## Temel kavramlar

- **Query (Q):** Hangi bilgi aranıyor?
- **Key (K):** Her token hangi bilgiyle eşleşir?
- **Value (V):** Attention sonucunda taşınacak içerik nedir?
- **Attention ağırlıkları:** Query ile key uyumlarının softmax ile olasılığa dönüştürülmüş hâli.

Attention ağırlığı açıklama için faydalı bir ipucu sunar; tek başına model kararının tam açıklaması değildir.
