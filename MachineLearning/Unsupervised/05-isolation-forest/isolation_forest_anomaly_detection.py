import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.ensemble import IsolationForest


def run_isolation_forest():
    # 1. Normal Veri ve Anomali (Outlier) Üretimi
    # 250 adet normal veri noktası (yoğun bir küme halinde)
    np.random.seed(42)
    X_normal, _ = make_blobs(n_samples=250, centers=1, cluster_std=1.0, random_state=42)
    
    # Kümenin çok dışına düşecek şekilde 25 adet yapay anomali (outlier) üretimi
    X_anomalies = np.random.uniform(low=-6, high=6, size=(25, 2))
    
    # Normal veriler ile anomalileri birleştirme
    X = np.r_[X_normal, X_anomalies]

    print("--- Veri Kümesi Özeti ---")
    print(f"Normal Veri Noktası Sayısı: {len(X_normal)}")
    print(f"Enjekte Edilen Anomali Sayısı: {len(X_anomalies)}")
    print(f"Toplam Veri Sayısı: {len(X)}")

    # 2. Model Kurulumu ve Eğitimi
    # contamination: Veri setindeki beklenen anomali oranı. (25 / 275 ≈ 0.09)
    # n_estimators: Ormandaki izolasyon ağacı (iTree) sayısı.
    # Ağaç tabanlı bir model olduğu için verinin ölçeklendirilmesine (scaling) ihtiyaç duymaz.
    model = IsolationForest(n_estimators=100, contamination=0.09, random_state=42)
    model.fit(X)

    # 3. Anomali Tahminleri ve Skorları
    # predict: Normal noktalar için 1, anomaliler için -1 çıktısı verir.
    predictions = model.predict(X)
    
    # decision_function: Noktaların anomali skorunu verir. 
    # Skor ne kadar düşükse (negatifse) o nokta o kadar izoledir (anomalidir).
    anomaly_scores = model.decision_function(X)

    # Sonuçların Özeti
    n_detected_anomalies = list(predictions).count(-1)
    n_detected_normals = list(predictions).count(1)
    
    print("\n--- Model Tahmin Sonuçları ---")
    print(f"Tespit Edilen Normal Nokta Sayısı (1): {n_detected_normals}")
    print(f"Tespit Edilen Anomali Noktası Sayısı (-1): {n_detected_anomalies}")

    # 4. Karar Sınırları İçin Arka Plan Matrisi (Contour Grid)
    # İzolasyon Ormanı'nın 2B uzayda çizdiği karar sınırlarını görselleştirmek için ağ örüntüsü oluşturulur
    xx, yy = np.meshgrid(np.linspace(-8, 8, 200), np.linspace(-8, 8, 200))
    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # 5. Görselleştirme: Ham Veri ve Karar Sınırları Analizi
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: İşlem Öncesi Ham Veri
    axes[0].scatter(X_normal[:, 0], X_normal[:, 1], color="grey", alpha=0.6, label="Normal Küme Örnekleri")
    axes[0].scatter(X_anomalies[:, 0], X_anomalies[:, 1], color="black", marker="x", s=50, label="Gerçek Anomaliler")
    axes[0].set_title("Eğitim Öncesi Ham Veri Dağılımı")
    axes[0].set_xlabel("Öznitelik 1")
    axes[0].set_ylabel("Öznitelik 2")
    axes[0].legend()
    axes[0].grid(True)

    # Sağ Grafik: Isolation Forest Tahminleri ve Karar Sınırları (Contour)
    # Arka plana anomali skor yoğunluğunu temsil eden ısı haritası çizdirilir
    contour = axes[1].contourf(xx, yy, Z, cmap=plt.cm.Blues_r, alpha=0.5)
    fig.colorbar(contour, ax=axes[1], label="Anomali Skoru (Düşük Değer = Daha Anormal)")

    # Modelin 'normal' (1) ve 'anomali' (-1) olarak tahmin ettiği noktaların çizimi
    axes[1].scatter(
        X[predictions == 1, 0], 
        X[predictions == 1, 1], 
        color="green", 
        edgecolors="k", 
        alpha=0.8, 
        label="Tahmin: Normal (1)"
    )
    axes[1].scatter(
        X[predictions == -1, 0], 
        X[predictions == -1, 1], 
        color="red", 
        marker="o", 
        edgecolors="k", 
        s=50, 
        label="Tahmin: Anomali (-1)"
    )

    # Karar Sınırını (Skor = 0 çizgisi) belirginleştirmek için kırmızı çizgi eklenir
    axes[1].contour(xx, yy, Z, levels=[0], colors="red", linewidths=2, linestyles="dashed")

    axes[1].set_title("Isolation Forest Karar Sınırları ve Anomali Tahminleri")
    axes[1].set_xlabel("Öznitelik 1")
    axes[1].set_ylabel("Öznitelik 2")
    axes[1].legend(loc="lower left")
    axes[1].grid(True)

    plt.tight_layout()
    output_image = "isolation_forest_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_isolation_forest()