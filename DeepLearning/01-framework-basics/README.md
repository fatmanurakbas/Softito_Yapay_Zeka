# Deep Learning 01 — Framework Temelleri

Bu çalışma PyTorch ile tensor işlemleri, otomatik türev, Dataset/DataLoader ve eğitim adımının temel akışını öğretir.

```text
01-framework-basics/
├── 01-tensors/
├── 02-autograd/
├── 03-dataset-dataloader/
├── 04-training-step/
└── tests/
```

```bash
cd DeepLearning/01-framework-basics
pip install -r requirements.txt
python 01-tensors/tensor_basics.py
python 02-autograd/autograd_basics.py
python 03-dataset-dataloader/dataloader_basics.py
python 04-training-step/training_step.py
```

Tensorların cihazını ve veri tipini görünür tutun. `requires_grad=True` olan tensorlar için autograd işlem grafiği kurar; `loss.backward()` sonrasında gradient değerleri erişilebilir olur. Eğitim döngüsünde doğru sıralama `zero_grad → forward → loss → backward → optimizer.step` şeklindedir.
