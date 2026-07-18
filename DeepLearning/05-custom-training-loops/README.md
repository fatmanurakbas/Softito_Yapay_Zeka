# Deep Learning 05 — Özel Eğitim Döngüleri

Özel eğitim döngüsü, forward pass, loss, backward, optimizer, doğrulama, checkpoint ve loglama adımlarını doğrudan kontrol etmenizi sağlar.

```text
05-custom-training-loops/
├── 01-train-validate/       # Açık train/validation döngüsü
├── 02-checkpoint-resume/    # Checkpoint kaydetme ve yükleme
├── 03-training-techniques/  # Gradient clipping ve accumulation
├── checkpoints/             # Çalışma zamanı çıktıları (Git dışı)
└── tests/
```

```bash
cd DeepLearning/05-custom-training-loops
python 01-train-validate/train_validate.py
python 02-checkpoint-resume/checkpoint_resume.py
python 03-training-techniques/gradient_techniques.py
```

Temel sıra: `model.train() → zero_grad → forward → loss → backward → optimizer.step`; doğrulamada `model.eval()` ve `torch.no_grad()` kullanılır. Checkpoint'e model, optimizer, epoch ve metrik birlikte kaydedilmelidir.
