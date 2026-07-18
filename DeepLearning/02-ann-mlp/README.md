# Deep Learning 02 — ANN ve MLP

Çok katmanlı algılayıcı (MLP), tam bağlı katmanlar ve doğrusal olmayan aktivasyonlarla karmaşık karar sınırlarını öğrenir. Bu çalışma mimari, tablosal sınıflandırma ve düzenlileştirmeyi sırayla uygular.

```text
02-ann-mlp/
├── 01-xor-mlp/               # Doğrusal olmayan XOR problemi
├── 02-tabular-classification/# Sentetik tablosal sınıflandırma
├── 03-regularization/        # Dropout ve BatchNorm karşılaştırması
└── tests/
```

```bash
cd DeepLearning/02-ann-mlp
pip install -r requirements.txt
python 01-xor-mlp/xor_mlp.py
python 02-tabular-classification/tabular_mlp.py
python 03-regularization/regularization_comparison.py
```

MLP için giriş özelliklerini ölçeklemek, doğrulama setini eğitimden ayırmak ve çıktı katmanını görev türüne uygun seçmek önemlidir. İkili sınıflandırmada `BCEWithLogitsLoss`, sigmoid katmanını kayıp hesabıyla birlikte güvenli biçimde uygular.
