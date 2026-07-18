# Deep Learning 03 — CNN

CNN'ler görüntüdeki yerel örüntüleri convolution filtreleriyle öğrenir. Bu çalışma convolution çıktısını, küçük bir görüntü sınıflandırıcısını ve veri artırmanın etkisini uygulamalı olarak gösterir.

```text
03-cnn/
├── 01-convolution/          # Kernel, padding, stride
├── 02-image-classification/ # Sentetik çizgi görselleriyle CNN
├── 03-augmentation/         # Flip ve gürültü artırması
└── tests/
```

```bash
cd DeepLearning/03-cnn
pip install -r requirements.txt
python 01-convolution/convolution_basics.py
python 02-image-classification/cnn_classifier.py
python 03-augmentation/augmentation.py
```

Convolution katmanı kanal sayısını ve uzamsal boyutu dönüştürür; pooling boyutu azaltır. Gerçek görüntü verisinde eğitim/validation ayrımını koruyun ve sadece eğitim verisine augmentation uygulayın.
