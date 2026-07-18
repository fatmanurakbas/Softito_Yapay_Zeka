# Churn Prediction Platform — Mikroservisler

Bu proje, müşteri terk tahminini üç ayrı model servisi üzerinden sunan Docker Compose tabanlı bir platform örneğidir. Gateway isteği model servislerine iletir, sonuçları PostgreSQL'e kaydeder ve birleşik yanıt döndürür.

## Mimari

```text
İstemci
  │ POST /predict
  ▼
Gateway API :8000 ──► Logistic Service :8000
  │                  ► Random Forest Service :8000
  │                  ► XGBoost Service :8000
  └─────────────────► PostgreSQL :5432
                         ▲
                    pgAdmin :5050
```

## Klasör yapısı

```text
ml-churn-platform/
├── gateway/             # İstek yönlendirme ve tahmin kaydı
├── logistic_service/    # Logistic Regression API ve modeli
├── rf_service/          # Random Forest API ve modeli
├── xgb_service/         # XGBoost API ve modeli
├── training/            # Model eğitim betikleri
├── data/                # Telco churn veri kümesi
└── docker-compose.yml   # Tüm platform servisleri
```

## Başlatma

```powershell
docker compose up --build
```

İlk imaj oluşturma işlemi sürebilir. Çalışan servisleri görmek için:

```powershell
docker compose ps
```

Durdurmak için:

```powershell
docker compose down
```

PostgreSQL hacmini de silmek gerektiğinde `docker compose down -v` kullanılır. Bu, kayıtlı tahmin verilerini kalıcı olarak kaldırır.

## Servisler

| Servis | Adres | Sorumluluk |
|---|---|---|
| Gateway | `http://localhost:8000` | Tahmin isteğini dağıtır ve sonuçları kaydeder. |
| PostgreSQL | `localhost:5432` | `predictions` tablosunu tutar. |
| pgAdmin | `http://localhost:5050` | PostgreSQL yönetim arayüzü. |
| Logistic / RF / XGBoost | Yalnız Compose ağı içinde | Bireysel model tahminleri. |

Gateway API dokümanı: `http://localhost:8000/docs`

## Tahmin isteği

```powershell
$body = @{
  gender = "Female"; SeniorCitizen = 0; Partner = "Yes"; Dependents = "No"
  tenure = 12; PhoneService = "Yes"; MultipleLines = "No"
  InternetService = "Fiber optic"; OnlineSecurity = "No"; OnlineBackup = "Yes"
  DeviceProtection = "No"; TechSupport = "No"; StreamingTV = "Yes"; StreamingMovies = "Yes"
  Contract = "Month-to-month"; PaperlessBilling = "Yes"; PaymentMethod = "Electronic check"
  MonthlyCharges = 85.5; TotalCharges = 1026.0
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri http://localhost:8000/predict -ContentType "application/json" -Body $body
```

Gateway, `logistic`, `random_forest` ve `xgboost` anahtarları altında her modelin sınıf tahminini ve olasılığını döndürür. Ayrıca her sonuç PostgreSQL'deki `predictions` tablosuna yazılır.

## Model eğitimi

`training` klasöründe bulunan `train_logistic.py`, `train_rf.py` ve `train_xgb.py` betikleri Telco Customer Churn verisi üzerinde model üretmek içindir. Yeni model dosyası oluştuğunda ilgili servisin imajını yeniden oluşturun:

```powershell
docker compose up --build
```

## Geliştirme notu

Compose dosyasında yer alan PostgreSQL ve pgAdmin bilgileri yerel geliştirme amacıyla örnek değerlerdir. Bu değerleri sürüm kontrolüne uygun olmayan `.env` dosyasına taşıyıp gerçek ortamlarda secret yönetimi kullanın.
