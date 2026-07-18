# NLP 05 — Long Short-Term Memory (LSTM)

LSTM, klasik RNN'in uzun dizilerde yaşadığı bilgi ve gradient kaybını kapı mekanizmalarıyla hafifletir. Hücre durumu (`c_t`) bilgiyi taşırken forget, input ve output kapıları hangi bilginin silinip ekleneceğini öğrenir.

Mevcut `LSTM.ipynb` not defteri korunmuştur. Bu klasörlerdeki Python örnekleri konuyu küçük ve tekrarlanabilir deneylerle tamamlar.

## Klasör yapısı

```text
05-lstm/
├── 01-lstm-cell/                  # Forget/input/output kapıları
├── 02-sentiment-classification/   # NumPy ile LSTM + BPTT
├── 03-memory-flow/                # RNN ve LSTM bellek karşılaştırması
├── data/sentiment.csv
├── figures/
└── requirements.txt
```

## Çalıştırma

```bash
cd NLP/05-lstm
python 01-lstm-cell/lstm_cell.py
python 02-sentiment-classification/train_lstm.py
python 03-memory-flow/memory_flow.py
```

## RNN'den farkı

RNN'de tek gizli durum her adımda yeniden yazılır. LSTM'de hücre durumu, forget gate değeri yüksek kaldığında çok sayıda zaman adımı boyunca bilgiyi koruyabilir. Bu, uzun bağlamlı metinlerde daha kararlı eğitim sağlar; yine de Transformer'lar çok uzun bağlamlarda çoğu zaman daha uygundur.
