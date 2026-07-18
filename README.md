<<<<<<< HEAD
# Softito Yapay Zeka Öğrenme Deposu

Bu depo; makine öğrenmesi, derin öğrenme, doğal dil işleme, büyük dil modelleri, küçük dil modelleri, büyük veri, web scraping ve Docker ile model servisleştirme konularını uygulamalı olarak çalışmak için hazırlanmış Türkçe bir eğitim alanıdır.

Her bölüm, konuyu küçük adımlara ayırır. Çoğu konuda bir `README.md`, çalıştırılabilir Python örnekleri, gerekli olduğunda `requirements.txt` ve kısa doğrulama/test dosyaları bulunur.

## İçerik haritası

| Klasör | Kapsam | Öne çıkan konular |
|---|---|---|
| [MachineLearning](MachineLearning) | Klasik makine öğrenmesi | Regresyon, sınıflandırma, ağaçlar, SVM, KNN, model seçimi |
| [NLP](NLP) | Doğal dil işleme | Ön işleme, TF-IDF, embedding, RNN, LSTM, attention, BERT |
| [LLM](LLM) | Büyük dil modeli uygulamaları | Prompt engineering, RAG, vektör veritabanı, LangChain, LoRA, DPO |
| [SLM](SLM) | Yerel ve küçük dil modelleri | Ollama, GGUF nicemleme, Türkçe SLM projesi |
| [DeepLearning](DeepLearning) | Derin öğrenme | PyTorch temelleri, MLP, CNN, GRU, özel eğitim döngüleri |
| [BigData](BigData) | Dağıtık veri sistemleri | HDFS, Spark, Kafka, Airflow, Lakehouse, Delta Lake, MLOps |
| [WebScraping](WebScraping) | Sorumlu web verisi toplama | Requests, Beautiful Soup, API, Playwright, veri temizleme |
| [Docker](Docker) | Model servisleştirme | FastAPI, Docker Compose, PostgreSQL, mikroservisler |
| [.agents](.agents) | Ajan çalışma notları | Kodlama kuralları, proje haritası, görev şablonları |

## Öğrenme akışı

Başlangıç için önerilen sıra:

1. `MachineLearning` ile klasik modelleme kavramlarını öğrenin.
2. `DeepLearning` ile PyTorch ve sinir ağları pratiği yapın.
3. `NLP` ile metin verisini modellemeye geçin.
4. `LLM` ve `SLM` ile üretken yapay zekâ uygulamalarını çalışın.
5. `BigData` ile veri altyapısı ve dağıtık işlemeyi öğrenin.
6. `Docker` ile modelleri API olarak paketleyin ve çalıştırın.
7. `WebScraping` ile izinli kaynaklardan veri toplama pratiği yapın.

Bu sıra zorunlu değildir. Her klasör kendi README dosyası üzerinden bağımsız biçimde çalışılabilir.

## Klasör yapısı

```text
Softito_Yapay_Zeka/
├── MachineLearning/
│   ├── Supervised/
│   └── Unsupervised/
├── NLP/
├── LLM/
├── SLM/
├── DeepLearning/
├── BigData/
├── WebScraping/
├── Docker/
└── .agents/
```

## Çalışma yaklaşımı

- Önce ilgili klasörün README dosyasını okuyun.
- Gerekirse o klasördeki bağımlılıkları kurun:

  ```powershell
  python -m pip install -r requirements.txt
  ```

- Ardından örnek Python dosyasını çalıştırın.
- Haricî servis kullanan bölümlerde (Docker, Ollama, Spark, Airflow, Playwright gibi) ilgili servisin ayrıca kurulması gerekebilir.
- Büyük model indirme, API anahtarı veya ağ erişimi isteyen örnekleri yerel ortamınıza göre yapılandırın.

## Önemli notlar

- Örnekler eğitim amaçlıdır; üretim sistemleri için ek güvenlik, gözlemlenebilirlik, test ve hata yönetimi gerekir.
- Web scraping çalışmalarında `robots.txt`, kullanım koşulları, hız limiti ve kişisel veri ilkelerine uyun.
- `.env`, erişim anahtarları, geçici çıktılar ve yerel veritabanı dosyaları genel `.gitignore` ile sürüm kontrolü dışında tutulur.
- Docker altındaki model dosyaları proje örneklerinin çalışması için korunur.

## Docker projeleri

`Docker` dizininde iki churn tahmin örneği vardır:

- [Tek servis FastAPI uygulaması](Docker/ml_projem/README.md)
- [Gateway ve üç model servisi içeren mikroservis platformu](Docker/ml-churn-platform/README.md)
