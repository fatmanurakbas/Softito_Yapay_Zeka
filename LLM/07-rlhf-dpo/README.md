# LLM 07 — RLHF ve DPO

Bu çalışma, insan tercihlerinden oluşturulan `chosen/rejected` yanıt çiftleriyle Direct Preference Optimization (DPO) uygulamasını hazırlar. DPO, ayrı bir reward model eğitmeden tercih çiftleri üzerinden politika davranışını doğrudan iyileştirmeyi hedefler.

## Çalışma akışı

```text
07-rlhf-dpo/
├── configs/dpo_config.json
├── data/preferences.jsonl
├── 01-data-preparation/      # Tercih çifti doğrulaması
├── 02-training/              # TRL DPOTrainer eğitimi
├── 03-evaluation/            # Tercih kazanımını hesaplama
├── adapters/                 # Eğitim çıktıları
└── tests/
```

```bash
cd LLM/07-rlhf-dpo
pip install -r requirements.txt
python 01-data-preparation/validate_preferences.py
python 02-training/train_dpo.py
python 03-evaluation/evaluate_preferences.py --input data/preferences.jsonl
```

Tercih verisi, model davranışını doğrudan belirler. Her çiftte seçilen yanıtın neden daha iyi olduğunu; doğruluk, yararlılık, güvenlik ve üslup boyutlarında insan incelemesiyle denetleyin.
