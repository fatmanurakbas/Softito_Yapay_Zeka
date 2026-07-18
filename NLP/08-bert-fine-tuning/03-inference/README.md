# 03 — Tahmin

Eğitilmiş model klasörünü ve aynı tokenizer'ı kullanarak tek bir metin için pozitif/negatif olasılıkları üretin.

```bash
python predict.py --text "Ürün kaliteli ve kargo hızlıydı"
```

Tahmin olasılığı güvenilirlik garantisi değildir. Özellikle eğitim verisinin dışındaki alanlarda örnek bazlı hata analizi yapın.
