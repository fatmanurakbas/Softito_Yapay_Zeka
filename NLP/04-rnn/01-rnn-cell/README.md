# 01 — RNN Hücresi

Bir RNN hücresi her zaman adımında yeni girdiyi (`x_t`) ve önceki gizli durumu (`h_{t-1}`) birleştirir:

`h_t = tanh(W_x x_t + W_h h_{t-1} + b)`

Bu betik, küçük sayısal tensörlerle üç zaman adımı için forward pass yapar.

```bash
python rnn_cell.py
```
