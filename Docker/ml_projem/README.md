# Churn Prediction API — Tek Servis

Bu proje, eğitilmiş `churn_model.pkl` dosyasını kullanan basit bir FastAPI tahmin servisi ve PostgreSQL veritabanından oluşur. Docker Compose, iki servisi aynı ağda başlatır.

## Yapı

```text
ml_projem/
├── app.py                 # FastAPI uygulaması
├── churn_model.pkl        # Eğitilmiş model
├── requirements.txt       # Python bağımlılıkları
├── Dockerfile             # API imajı
└── docker-compose.yml     # API + PostgreSQL
```

## Çalıştırma

Docker Desktop açıkken bu klasörde aşağıdaki komutu çalıştırın:

```powershell
docker compose up --build
```

API: `http://localhost:8000`  
Swagger arayüzü: `http://localhost:8000/docs`

Konteynerleri durdurmak için:

```powershell
docker compose down
```

## Uç noktalar

| Metot | Yol | Açıklama |
|---|---|---|
| `GET` | `/` | Servisin çalıştığını doğrular. |
| `POST` | `/predict` | Müşteri verisinden churn tahmini üretir. |

## Tahmin örneği

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

Örnek yanıt:

```json
{"prediction": 1}
```

`1`, müşterinin ayrılma olasılığına ilişkin model sınıfını; `0` ise ayrılmama sınıfını temsil eder. Bu etiketlerin iş anlamı eğitim aşamasında kullanılan veri tanımına göre değerlendirilmelidir.

## PostgreSQL

Veritabanı `localhost:5432` üzerinden erişilebilir. Varsayılan geliştirme bilgileri Compose dosyasında tanımlıdır. Gerçek projelerde bu bilgileri `.env` veya bir secret yöneticisi üzerinden sağlayın.
