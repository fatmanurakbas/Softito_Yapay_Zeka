# 01 — Veri Hazırlama

Ham CSV, etiket dağılımını koruyacak şekilde eğitim, validation ve test kümelerine ayrılır. Kod, etiketleri `0/1` olarak bekler ve aynı seed ile tekrarlanabilir sonuç verir.

```bash
python prepare_data.py
```

Çıktılar `data/processed/` altına yazılır. Ön işlemeyi eğitimden önce sabitleyin; test örneklerinin çoğaltılmış veya neredeyse aynı sürümlerinin eğitimde olmadığını denetleyin.
