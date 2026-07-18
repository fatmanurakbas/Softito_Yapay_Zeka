import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


def create_messy_dataset():
    # Gerçek hayat senaryosunu taklit eden kirli ve eksik değerlere sahip yapay bir veri kümesi oluşturma
    np.random.seed(42)
    data = {
        "id": range(1, 101),
        "age": [np.random.choice([25, 30, 35, 40, np.nan]) for _ in range(100)],
        "salary": [np.random.choice([30000, 45000, 60000, 80000, 999999, np.nan]) for _ in range(100)], # 999999 aykırı değerdir
        "experience_years": np.random.randint(1, 15, size=100).astype(float),
        "education_level": [np.random.choice(["High School", "Bachelor", "Master", "PhD"]) for _ in range(100)], # Ordinal
        "department": [np.random.choice(["IT", "Sales", "HR", np.nan]) for _ in range(100)], # Nominal + Eksik Değer
    }
    # Belirli hücrelere rastgele boş değerler (NaN) atama
    df = pd.DataFrame(data)
    df.loc[df["experience_years"] > 12, "experience_years"] = np.nan
    return df


def run_feature_engineering():
    # 1. Kirli Veri Kümesini Yükleme
    df_raw = create_messy_dataset()
    df = df_raw.copy()

    print("--- Ham Veri Kümesi (İlk 5 Satır) ---")
    print(df.head())
    print("\nEksik Değerlerin Dağılımı:")
    print(df.isnull().sum())

    # --- ADIM 1: Eksik Değerlerin Doldurulması (Imputation) ---
    # Sayısal Değişkenler: Medyan ile doldurulur (Aykırı değerlerden etkilenmemesi için)
    num_cols = ["age", "experience_years", "salary"]
    num_imputer = SimpleImputer(strategy="median")
    df[num_cols] = num_imputer.fit_transform(df[num_cols])

    # Kategorik Değişkenler: En sık tekrar eden değer (mode) ile doldurulur
    cat_imputer = SimpleImputer(strategy="most_frequent")
    df[["department"]] = cat_imputer.fit_transform(df[["department"]])

    # --- ADIM 2: Aykırı Değerlerin Törpülenmesi (Outlier Capping - IQR Method) ---
    # Maaş kolonundaki 999999 gibi uç değerleri veriden silmek yerine IQR sınırlarına sıkıştıracağız (Winsorization)
    Q1 = df["salary"].quantile(0.25)
    Q3 = df["salary"].quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    # Sınırların dışındaki değerleri alt ve üst limitlere eşitleme
    df["salary"] = np.clip(df["salary"], lower_limit, upper_limit)

    # --- ADIM 3: Kategorik Değişken Kodlama (Encoding) ---
    # A) Ordinal Encoding (Dereceli Kategorik): Eğitim seviyeleri hiyerarşik sıralanır
    education_order = ["High School", "Bachelor", "Master", "PhD"]
    ordinal_enc = OrdinalEncoder(categories=[education_order])
    df["education_encoded"] = ordinal_enc.fit_transform(df[["education_level"]])

    # B) One-Hot Encoding (Sıralaması Olmayan Kategorik): Departmanlar ikili (binary) matrise çevrilir
    one_hot_enc = OneHotEncoder(sparse_output=False, drop="first")  # Kukla değişken tuzağını önlemek için drop='first'
    dept_encoded = one_hot_enc.fit_transform(df[["department"]])
    dept_encoded_df = pd.DataFrame(
        dept_encoded, 
        columns=one_hot_enc.get_feature_names_out(["department"]),
        index=df.index
    )
    df = pd.concat([df, dept_encoded_df], axis=1)

    # --- ADIM 4: Yeni Özniteliklerin Üretilmesi (Feature Creation) ---
    # Mevcut özniteliklerin etkileşiminden yeni ve daha açıklayıcı değişkenler üretme
    # A) Tecrübe yılı başına düşen maaş oranı (Verimlilik/Değer göstergesi)
    # Sıfıra bölme hatasını önlemek için küçük bir sabit (epsilon) eklenmiştir.
    df["salary_per_experience"] = df["salary"] / (df["experience_years"] + 0.1)

    # B) Yaşa ve tecrübeye göre Kıdemlilik Bayrağı (Seniority Flag)
    df["is_senior"] = ((df["age"] >= 35) & (df["experience_years"] >= 8)).astype(int)

    # --- ADIM 5: Özellik Ölçeklendirme (Feature Scaling) ---
    # Sayısal kolonların son hallerini ölçeklendiriyoruz
    scale_cols = ["age", "salary", "experience_years", "salary_per_experience"]
    scaler = StandardScaler()
    df_scaled_cols = pd.DataFrame(
        scaler.fit_transform(df[scale_cols]),
        columns=[f"{col}_scaled" for col in scale_cols],
        index=df.index
    )
    df = pd.concat([df, df_scaled_cols], axis=1)

    # --- SONUÇLARIN GÖSTERİLMESİ ---
    print("\n--- Öznitelik Mühendisliği Sonrası Veri Kümesi (İlk 5 Satır) ---")
    processed_cols = [
        "age_scaled", "salary_scaled", "experience_years_scaled", 
        "education_encoded", "department_IT", "salary_per_experience_scaled", "is_senior"
    ]
    # Sadece dönüştürülen ve modelin doğrudan kabul edebileceği kolonları yazdırıyoruz
    print(df[processed_cols].head())

    # 6. Görselleştirme: Outlier Törpüleme Öncesi ve Sonrası Maaş Dağılımı
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Sol Grafik: İşlem Öncesi Maaş Dağılımı (Kutu Grafiği)
    axes[0].boxplot(df_raw["salary"].dropna(), patch_artist=True, boxprops=dict(facecolor="salmon"))
    axes[0].set_title("İşlem Öncesi Maaş Dağılımı (Aykırı Değerli)")
    axes[0].set_ylabel("Maaş Tutarı")

    # Sağ Grafik: İşlem Sonrası Ölçeklenmiş Maaş Dağılımı (Kutu Grafiği)
    axes[1].boxplot(df["salary_scaled"], patch_artist=True, boxprops=dict(facecolor="lightblue"))
    axes[1].set_title("İşlem Sonrası Standartlaştırılmış Maaş Dağılımı")
    axes[1].set_ylabel("Maaş (Standartlaştırılmış)")

    plt.tight_layout()
    output_image = "feature_engineering_transformation.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_feature_regression = run_feature_engineering()