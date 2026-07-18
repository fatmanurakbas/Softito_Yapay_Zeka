# NLP 08 — BERT Fine-Tuning

Bu çalışma, önceden eğitilmiş bir BERT modelini Türkçe ikili duygu sınıflandırması için uyarlayan uçtan uca bir proje iskeletidir. Ön eğitimden gelen dil bilgisini korurken, sınıflandırma başlığı hedef veri setinizde eğitilir.

## Klasör yapısı

```text
08-bert-fine-tuning/
├── 01-data-preparation/        # Stratified train/validation/test ayrımı
├── 02-training/                # Hugging Face Trainer ile fine-tuning
├── 03-inference/               # Kayıtlı modelle tekil tahmin
├── 04-evaluation/              # Accuracy, precision, recall, F1
├── data/raw_reviews.csv         # Küçük örnek Türkçe yorum verisi
├── models/                      # Eğitilen checkpoint'ler (Git'e eklenmez)
└── requirements.txt
```

## Kurulum ve çalışma sırası

```bash
cd NLP/08-bert-fine-tuning
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python 01-data-preparation/prepare_data.py
python 02-training/train.py --model-name dbmdz/bert-base-turkish-cased
python 03-inference/predict.py --text "Ürün kaliteli ve kargo hızlıydı"
python 04-evaluation/evaluate.py
```

İlk eğitimde model/tokenizer indirileceği için internet bağlantısı gerekir. GPU varsa PyTorch uygun CUDA kurulumuyla eğitimi hızlandırır; CPU ile de küçük veri setlerinde deney yapılabilir.

## Dikkat edilmesi gerekenler

- Test kümesini model, eşik veya hiperparametre seçmek için kullanmayın.
- `max_length`, öğrenme oranı, batch size ve epoch sayısını validation setine göre ayarlayın.
- Accuracy tek başına yeterli değildir; dengesiz sınıflarda macro F1 ve hata analizi ekleyin.
- Üretimde tokenizer ve model klasörünü birlikte sürümleyin; eğitim verisinin kaynağını ve lisansını belgeleyin.
