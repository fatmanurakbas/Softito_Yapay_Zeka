# NLP 04 — Recurrent Neural Networks (RNN)

RNN'ler sıradaki tokenları birer birer işler ve önceki adımlardan gelen bilgiyi gizli durumda (`h_t`) taşır. Bu çalışma RNN hücresinin matematiğini, BPTT (zaman boyunca geri yayılım) eğitimini ve uzun dizilerdeki gradient sorununu uygulamalı olarak ele alır.

Mevcut `RNN.ipynb` not defteri korunmuştur; aşağıdaki klasörler bağımsız ve tekrarlanabilir Python çalışmalarıdır.

## Klasör yapısı

```text
04-rnn/
├── 01-rnn-cell/                   # Tek adımlı RNN forward pass
├── 02-sentiment-classification/   # NumPy ile BPTT ve duygu sınıflandırma
├── 03-gradient-flow/              # Vanishing/exploding gradient gözlemi
├── data/sentiment.csv             # Küçük Türkçe eğitim verisi
├── figures/                       # Üretilecek görseller
├── RNN.ipynb                      # Mevcut not defteri
└── requirements.txt
```

## Çalıştırma

```bash
cd NLP/04-rnn
python 01-rnn-cell/rnn_cell.py
python 02-sentiment-classification/train_rnn.py
python 03-gradient-flow/gradient_flow.py
```

## Öğrenme notları

- Her cümlede token sayısı değiştiği için bu küçük örnek padding kullanmadan tek tek dizileri işler. Batch eğitiminde padding ve mask kullanmanız gerekir.
- RNN'ler uzun bağımlılıklarda zorlanabilir. Bunun nedeni gradient'in zaman adımları boyunca tekrar tekrar çarpılmasıdır.
- Sonraki klasör olan LSTM, bu sorunu kapı mekanizmalarıyla hafifletir.
