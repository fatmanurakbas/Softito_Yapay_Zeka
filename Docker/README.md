# Docker Projeleri

Bu dizin, müşteri terk (churn) tahmin modellerini Docker ile çalıştıran iki FastAPI projesini içerir. İlk proje tek API konteyneriyle temel dağıtımı gösterir; ikinci proje ise üç modelin ayrı servisler olarak çalıştığı küçük bir mikroservis platformudur.

## Projeler

| Proje | Açıklama | Başlatma |
|---|---|---|
| [`ml_projem`](ml_projem/README.md) | Tek FastAPI tahmin API'si ve PostgreSQL | `docker compose up --build` |
| [`ml-churn-platform`](ml-churn-platform/README.md) | Gateway, Logistic Regression, Random Forest, XGBoost, PostgreSQL ve pgAdmin | `docker compose up --build` |

## 1. Tek servis: `ml_projem`

Bu uygulama, `churn_model.pkl` modelini açar ve `/predict` uç noktasında müşteri bilgisinden tahmin üretir. PostgreSQL konteyneri aynı Compose ağı içinde başlatılır.

```powershell
cd Docker/ml_projem
docker compose up --build
```

API adresi: `http://localhost:8000`  
Etkileşimli API dokümanı: `http://localhost:8000/docs`

```powershell
docker compose down
```

## 2. Mikroservis platformu: `ml-churn-platform`

Platformda istekler önce gateway'e gelir. Gateway aynı müşteri verisini üç model servisine iletir, sonuçları PostgreSQL'deki `predictions` tablosuna kaydeder ve tüm model yanıtlarını tek JSON içinde döndürür.

```text
İstemci -> Gateway:8000 -> Logistic:8000
                       -> Random Forest:8000
                       -> XGBoost:8000
                       -> PostgreSQL:5432
pgAdmin:5050 ----------> PostgreSQL:5432
```

Başlatma:

```powershell
cd Docker/ml-churn-platform
docker compose up --build
```

| Servis | Yerel adres | Görev |
|---|---|---|
| Gateway | `http://localhost:8000` | İstek yönlendirme ve sonuç kaydı |
| PostgreSQL | `localhost:5432` | Tahmin kayıtları |
| pgAdmin | `http://localhost:5050` | Veritabanı arayüzü |
| Model servisleri | Compose ağı içinde | Logistic, Random Forest ve XGBoost tahminleri |

Varsayılan pgAdmin hesabı Compose dosyasında tanımlıdır: `admin@admin.com` / `admin123`. Bu bilgiler yalnızca yerel geliştirme içindir; gerçek ortamlarda ortam değişkenleri veya bir secret yöneticisi kullanın.

## Tahmin isteği örneği

Platform çalışırken aşağıdaki isteği gateway'e gönderebilirsiniz:

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

Yanıt, her model için `model`, `prediction` ve `probability` alanlarını içerir. Tek servis projesinin yanıtı yalnızca `prediction` alanını döndürür.

## Eğitim ve modeller

`ml-churn-platform/training` altında Logistic Regression, Random Forest ve XGBoost modellerini eğiten Python betikleri bulunur. Eğitim verisi `data/WA_Fn-UseC_-Telco-Customer-Churn.csv` dosyasıdır. Üretilen `.pkl` dosyaları ilgili model servislerinin çalışması için gereklidir.

## Durdurma ve temizleme

Konteynerleri durdurmak için:

```powershell
docker compose down
```

PostgreSQL verisini de silmek isterseniz `docker compose down -v` kullanılır. Bu işlem kalıcı veritabanı hacmini kaldırır.

## Notlar

- `docker compose config` ile Compose yapılandırmasını başlatmadan doğrulayabilirsiniz.
- Model dosyaları kaynakta mevcut olduğu için `.gitignore` tarafından yok sayılmaz.
- Şifre, `.env`, yerel veritabanı dökümü ve büyük geçici çıktılar Git'e eklenmez.
