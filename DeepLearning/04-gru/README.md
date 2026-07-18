# Deep Learning 04 — GRU

GRU (Gated Recurrent Unit), sıralı veride bilgiyi update ve reset kapılarıyla taşır. LSTM'e göre daha az parametre içerirken uzun bağımlılıkları klasik RNN'den daha iyi koruyabilir.

```text
04-gru/
├── 01-gru-cell/              # Kapıların forward pass'i
├── 02-sequence-classification/# PyTorch GRU sınıflandırıcısı
├── 03-architecture-comparison/# RNN/LSTM/GRU parametre sayısı
└── tests/
```

```bash
cd DeepLearning/04-gru
python 01-gru-cell/gru_cell.py
python 02-sequence-classification/gru_classifier.py
python 03-architecture-comparison/compare_recurrent_layers.py
```

GRU çıktısında son gizli durum sıralı sınıflandırma için kullanılabilir. Değişken uzunluklu gerçek dizilerde padding ve `pack_padded_sequence` gibi mekanizmalarla gereksiz zaman adımlarını maskeleyin.
