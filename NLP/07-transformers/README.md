# NLP 07 — Transformerlar

Transformer, sıralı veriyi tekrarlayan ağlar yerine self-attention ile işler. Token konumu positional encoding ile eklenir; encoder blokları çift yönlü bağlamı, decoder blokları ise causal mask ile önceki token bağlamını öğrenir.

## Klasör yapısı

```text
07-transformers/
├── 01-positional-encoding/   # Sıra bilgisinin vektörlere eklenmesi
├── 02-encoder-block/         # Multi-head attention + FFN + residual
├── 03-decoder-block/         # Causal self-attention ve sonraki token logits
├── figures/
└── requirements.txt
```

## Çalıştırma

```bash
cd NLP/07-transformers
python 01-positional-encoding/positional_encoding.py
python 02-encoder-block/transformer_encoder.py
python 03-decoder-block/transformer_decoder.py
```

## Mimari akış

1. Token embedding ve positional encoding toplanır.
2. Multi-head self-attention, tokenlar arası ilişkileri hesaplar.
3. Residual bağlantı ve layer normalization bilgiyi dengeler.
4. Position-wise feed-forward network her tokenı bağımsız dönüştürür.
5. Decoder'da causal mask gelecekteki tokenlara erişimi kapatır.

Bu örnekler forward pass mantığını açıklamak için NumPy ile yazılmıştır. Eğitim, tokenizer ve büyük ölçekli veri yönetimi sonraki BERT fine-tuning çalışmasında hazır framework'lerle ele alınacaktır.
