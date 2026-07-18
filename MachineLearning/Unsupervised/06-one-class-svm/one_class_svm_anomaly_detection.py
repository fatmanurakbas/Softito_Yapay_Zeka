import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM


def run_one_class_svm():
    # 1. Normal Veri ve Anomali (Outlier) Üretimi
    # Karşılaştırma amacıyla İzolasyon Ormanı'ndaki veri yapısının aynısı kurgulanmıştır.
    np.random.seed(42)
    X_normal, _ = make_blobs(n_samples=250, centers=1, cluster_std=1.0, random_state=42)
    
    # Kümenin dışına düşecek şekilde 25 adet yapay anomali (outlier) üretimi
    X_anomalies = np.random.uniform(low=-6, high=6, size=(25, 2))
    
    # Normal veriler ile anomalileri birleştirme
    X = np.r_[X_normal, X_anomalies]

    print("--- Veri Kümesi Özeti ---")
    print(f"Normal Veri Noktası Sayısı: {len(X_normal)}")
    print(f"Enjekte Edilen Anomali Sayısı: {len(X_anomalies)}")
    print(f"Toplam Veri Sayısı: {len(X)}")

    # 2. Öznitelik Ölçeklendirme (Feature Scaling)
    # One-Class SVM çekirdek (kernel) ve mesafe tabanlı bir modeldir.
    # Bu nedenle verinin standartlaştırılması modelin kararlı bir sınır çizebilmesi için ŞARTTIR.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. Model Kurulumu ve Eğitimi
    # nu: Eğitim setindeki izin verilen maksimum hata oranı (aykırı değer oranı). 25/275 ≈ 0.09
    # kernel='rbf': Doğrusal olmayan dairesel/organik karar sınırları çizebilmek için RBF çekirdeği tercih edilir.
    model = OneClassSVM(kernel="rbf", nu=0.09, gamma="scale")
    model.fit(X_scaled)

    # 4. Anomali Tahminleri ve Skorları
    # predict: Normal noktalar için 1, anomaliler için -1 çıktısı verir.
    predictions = model.predict(X_scaled)
    
    # score_samples: Noktaların karar düzlemine olan uzaklık skorunu (karar fonksiyonu çıktısını) verir.
    # Bu değer ne kadar negatifse nokta sınırın dışındadır (anomalidir).
    anomaly_scores = model.score_samples(X_scaled)

    # Sonuçların Özeti
    n_detected_anomalies = list(predictions).count(-1)
    n_detected_normals = list(predictions).count(1)
    
    print("\n--- Model Tahmin Sonuçları ---")
    print(f"Tespit Edilen Normal Nokta Sayısı (1): {n_detected_normals}")
    print(f"Tespit Edilen Anomali Noktası Sayısı (-1): {n_detected_anomalies}")

    # 5. Karar Sınırları İçin Arka Plan Matrisi (Contour Grid)
    # Grafik sınırları içinde bir örüntü ağı oluşturulup ölçeklendirilir ve modele tahmin ettirilir
    xx, yy = np.meshgrid(np.linspace(-8, 8, 200), np.linspace(-8, 8, 200))
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    grid_points_scaled = scaler.transform(grid_points)
    
    Z = model.decision_function(grid_points_scaled)
    Z = Z.reshape(xx.shape)

    # 6. Görselleştirme: Ham Veri ve One-Class SVM Sınırları Analizi
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: İşlem Öncesi Ham Veri
    axes[0].scatter(X_normal[:, 0], X_normal[:, 1], color="grey", alpha=0.6, label="Normal Küme Örnekleri")
    axes[0].scatter(X_anomalies[:, 0], X_anomalies[:, 1], color="black", marker="x", s=50, label="Gerçek Anomaliler")
    axes[0].set_title("Eğitim Öncesi Ham Veri Dağılımı")
    axes[0].set_xlabel("Öznitelik 1")
    axes[0].set_ylabel("Öznitelik 2")
    axes[0].legend()
    axes[0].grid(True)

    # Sağ Grafik: One-Class SVM Tahminleri ve Karar Sınırı (Contour)
    contour = axes[1].contourf(xx, yy, Z, cmap=plt.cm.Blues_r, alpha=0.5)
    fig.colorbar(contour, ax=axes[1], label="Karar Fonksiyonu Değeri (Negatif = Sınır Dışı)")

    # Modelin 'normal' (1) ve 'anomali' (-1) tahminleri çizdirilir
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

    # Modelin çizdiği organik karar sınırını (0 eşiği) kırmızı çizgiyle gösterme
    axes[1].contour(xx, yy, Z, levels=[0], colors="red", linewidths=2, linestyles="dashed")

    axes[1].set_title("One-Class SVM Karar Sınırları ve Tahminler")
    axes[1].set_xlabel("Öznitelik 1")
    axes[1].set_ylabel("Öznitelik 2")
    axes[1].legend(loc="lower left")
    axes[1].grid(True)

    plt.tight_layout()
    output_image = "one_class_svm_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_one_class_svm()