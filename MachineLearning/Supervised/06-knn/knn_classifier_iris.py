import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def run_knn_classifier():
    # 1. Veri Kümesini Yükleme
    # Scikit-learn kütüphanesindeki klasik Iris çiçek veri seti kullanılmıştır.
    # Hedef Değişken (Sınıf): 0 = Setosa, 1 = Versicolor, 2 = Virginica
    iris = load_iris(as_frame=True)
    df_x = iris.data
    df_y = iris.target

    print("--- Veri Kümesi Özeti ---")
    print(f"Öznitelik Sayısı: {df_x.shape[1]}")
    print(f"Örnek Sayısı: {df_x.shape[0]}")
    print(f"Sınıf Dağılımı:")
    print(df_y.value_counts().rename({0: "Setosa", 1: "Versicolor", 2: "Virginica"}))

    # 2. Eğitim ve Test Verisi Olarak Ayırma
    X_train, X_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size=0.2, random_state=42, stratify=df_y
    )

    # 3. Öznitelik Ölçeklendirme (Feature Scaling)
    # KNN, mesafe tabanlı çalıştığı için tüm özniteliklerin aynı ölçekte (aralıkta) olması şarttır.
    # Aksi takdirde, sayısal olarak büyük değerler alan öznitelikler mesafeyi domine eder.
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. K Değerinin Analizi (Hyperparameter Tuning)
    # Hangi komşuluk sayısının (K) en iyi performansı vereceğini görmek için 1'den 15'e kadar K değerleri test edilir.
    k_values = range(1, 16)
    accuracies = []

    for k in k_values:
        temp_model = KNeighborsClassifier(n_neighbors=k)
        temp_model.fit(X_train_scaled, y_train)
        y_temp_pred = temp_model.predict(X_test_scaled)
        accuracies.append(accuracy_score(y_test, y_temp_pred))

    # En iyi performansı veren ilk K değeri bulunur
    optimal_k = k_values[np.argmax(accuracies)]
    print(f"\nEn yüksek test doğruluğunu veren K değeri: {optimal_k}")

    # 5. Nihai Model Kurulumu ve Eğitimi
    # Optimal K değeri (veya varsayılan dengeli K=5) ile model kurulur.
    # metric='minkowski' ve p=2, Öklid (Euclidean) mesafesini temsil eder.
    model = KNeighborsClassifier(n_neighbors=optimal_k, metric="minkowski", p=2)
    model.fit(X_train_scaled, y_train)

    # 6. Tahmin Yapma
    y_pred = model.predict(X_test_scaled)

    # 7. Model Değerlendirme Metrikleri
    accuracy = accuracy_score(y_test, y_pred)
    print("\n--- Model Değerlendirme Sonuçları ---")
    print(f"Accuracy (Doğruluk):  {accuracy:.4f}")

    print("\n--- Detaylı Sınıflandırma Raporu ---")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # 8. Görselleştirme: Hata Matrisi ve K-Doğruluk Analiz Grafiği
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: Hata Matrisi (Confusion Matrix)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
    disp.plot(ax=axes[0], cmap=plt.cm.Reds, values_format="d")
    axes[0].set_title(f"Hata Matrisi (K = {optimal_k})")

    # Sağ Grafik: K Değeri vs. Test Doğruluğu
    axes[1].plot(k_values, accuracies, color="red", marker="o", linestyle="dashed", linewidth=2, markersize=8)
    axes[1].axvline(x=optimal_k, color="darkred", linestyle="--", label=f"Seçilen Optimal K ({optimal_k})")
    axes[1].set_xlabel("Komşu Sayısı (K Value)")
    axes[1].set_ylabel("Test Doğruluğu (Accuracy)")
    axes[1].set_title("K Değerinin Doğruluk Üzerindeki Etkisi")
    axes[1].set_xticks(k_values)
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    output_image = "knn_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_knn_classifier()