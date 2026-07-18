import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def run_linear_regression():
    # 1. Veri Kümesini Yükleme
    # Scikit-learn kütüphanesindeki hazır diyabet (diabetes) veri seti kullanılmıştır.
    # Bu veri seti 442 hastaya ait 10 temel klinik değişkeni (yaş, cinsiyet, BMI vb.)
    # ve 1 yıl sonraki hastalık ilerleme skorunu (hedef değişken) içerir.
    diabetes = load_diabetes(as_frame=True)
    df_x = diabetes.data
    df_y = diabetes.target

    print("--- Veri Kümesi Özeti ---")
    print(f"Öznitelik Sayısı: {df_x.shape[1]}")
    print(f"Örnek Sayısı: {df_x.shape[0]}")
    print("\nİlk 5 Satır (Öznitelikler):")
    print(df_x.head())

    # 2. Eğitim ve Test Verisi Olarak Ayırma
    # Verinin %80'i eğitim, %20'si test amacıyla ayrılmıştır.
    X_train, X_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size=0.2, random_state=42
    )

    # 3. Model Kurulumu ve Eğitimi
    # En Küçük Kareler (Ordinary Least Squares) yöntemiyle çalışan Doğrusal Regresyon modeli.
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 4. Tahmin Yapma
    y_pred = model.predict(X_test)

    # 5. Model Değerlendirme Metrikleri
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n--- Model Değerlendirme Sonuçları ---")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-squared (R2 Score): {r2:.4f}")

    # 6. Katsayılar (Coefficients) ve Kesişim Noktası (Intercept)
    print("\n--- Model Parametreleri ---")
    print(f"Kesişim Noktası (Intercept - Beta_0): {model.intercept_:.4f}")
    print("\nÖznitelik Katsayıları (Coefficients - Beta_i):")
    coef_df = pd.DataFrame(
        {"Öznitelik": df_x.columns, "Katsayı (Beta)": model.coef_}
    ).sort_values(by="Katsayı (Beta)", ascending=False)
    print(coef_df.to_string(index=False))

    # 7. Görselleştirme: Gerçek vs. Tahmin Edilen Değerler
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.7, color="b", label="Tahminler")
    
    # Kusursuz tahmin doğrusu (y_test == y_pred)
    ideal_line = np.linspace(min(y_test), max(y_test), 100)
    plt.plot(ideal_line, ideal_line, color="r", linestyle="--", label="İdeal Doğru")

    plt.xlabel("Gerçek Değerler (Disease Progression)")
    plt.ylabel("Tahmin Edilen Değerler")
    plt.title("Doğrusal Regresyon: Gerçek vs Tahmin Edilen Değerler")
    plt.legend()
    plt.grid(True)

    # Görseli çalışma dizinine kaydetme (GitHub'da göstermek için)
    output_image = "actual_vs_predicted.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_linear_regression()