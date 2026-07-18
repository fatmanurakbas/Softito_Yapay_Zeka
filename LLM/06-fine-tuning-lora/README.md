# LLM 06 — Fine-Tuning ve LoRA

Bu proje, temel modeli tamamen yeniden eğitmek yerine düşük-rank adapter ağırlıklarını eğiten LoRA akışını uygular. Amaç Türkçe talimat/yanıt verisini doğrulamak, adapter eğitmek ve adapter ile çıkarım yapmaktır.

## Akış

```text
06-fine-tuning-lora/
├── configs/training_config.json
├── data/train.jsonl
├── 01-data-preparation/     # Şema ve veri doğrulama
├── 02-training/             # Transformers + PEFT LoRA eğitimi
├── 03-inference/            # Base model + adapter yükleme
├── adapters/                # Eğitilen LoRA adapter'ları (Git dışı)
└── tests/
```

```bash
cd LLM/06-fine-tuning-lora
pip install -r requirements.txt
python 01-data-preparation/validate_dataset.py
python 02-training/train_lora.py
python 03-inference/generate.py --prompt "RAG nedir?"
```

Önce `configs/training_config.json` içindeki `base_model` ve `target_modules` değerlerini seçtiğiniz model mimarisine göre ayarlayın. LoRA yalnızca adapter parametrelerini eğitir; verinizin lisansı, kalitesi, test ayrımı ve güvenlik değerlendirmesi yine sizin sorumluluğunuzdadır.
