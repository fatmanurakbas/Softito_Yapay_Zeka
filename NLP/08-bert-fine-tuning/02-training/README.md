# 02 — Fine-Tuning Eğitimi

`train.py`, CSV bölmelerini Hugging Face `Dataset` nesnelerine dönüştürür, tokenizer uygular ve `AutoModelForSequenceClassification` modelini `Trainer` ile eğitir.

```bash
python train.py --model-name dbmdz/bert-base-turkish-cased --epochs 3 --batch-size 8
```

En iyi checkpoint validation macro F1'e göre seçilir. Küçük veri setinde metrikler yüksek oynaklık göstereceğinden sonuçları seed ve veri büyüklüğü bağlamında yorumlayın.
