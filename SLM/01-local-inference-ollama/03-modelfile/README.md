# 03 — Modelfile ile Özelleştirme

Modelfile, mevcut bir yerel modelin üzerine sistem davranışı ve üretim parametreleri eklemenizi sağlar. Önce `Modelfile` içindeki `FROM` satırını makinenizde bulunan model adıyla değiştirin.

```bash
ollama create turkce-asistan -f Modelfile
ollama run turkce-asistan
```

Sistem istemini dar, test edilebilir ve görev odaklı tutun. Modelfile davranışı model ağırlıklarını yeniden eğitmez; çıkarım zamanındaki şablon ve parametreleri yapılandırır.
