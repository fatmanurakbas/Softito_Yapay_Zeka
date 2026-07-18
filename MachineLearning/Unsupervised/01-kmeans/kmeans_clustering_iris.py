import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def run_kmeans_clustering():
    # 1. Veri Kümesini Yükleme
    # Gözetimsiz öğrenme yaptığımız için Iris veri kümesinin sadece özniteliklerini (X) kullanacağız.
    # Etiketleri (y) model eğitiminde tamamen göz ardı edeceğiz.
    iris = load_iris(as_frame=True)
    df_x = iris.data
    
    print("--- Veri Kümesi Özeti ---")
    print(f"Öznitelik Sayısı: {df_x.shape[1]}")
    print(f"Örnek Sayısı: {df_x.shape[0]}")
    print("\nİlk 5 Satır:")
    print(df_x.head())

    # 2. Öznitelik Ölçeklendirme (Feature Scaling)
    # K-Means, Öklid mesafesini temel alarak kümeleme yaptığı için standardizasyon zorunludur.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_x)

    # 3. Dirsek Yöntemi (Elbow Method) ile Optimal K Değerinin Belirlenmesi
    # 1'den 10'a kadar olan küme sayıları için "Inertia" (WCSS) değerleri hesaplanır.
    k_values = range(1, 11)
    inertias = []

    for k in k_values:
        # n_init='auto' veya n_init=10 belirtilerek uyarılar engellenir.
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)  # inertia_: Küme içi hata kareler toplamı (WCSS)

    # 4. Optimal K ile Kümeleme (Seçilen K = 3)
    # Dirsek noktasının 3 olduğunu varsayarak nihai kümeleme işlemini yapıyoruz.
    optimal_k = 3
    final_kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    cluster_labels = final_kmeans.fit_predict(X_scaled)

    # 5. Model Değerlendirmesi: Silhouette Skoru
    # Silhouette skoru, kümelerin ne kadar sıkı ve birbirinden ne kadar ayrık olduğunu ölçer.
    # +1 en iyi ayrımı, -1 hatalı kümelemeyi, 0 ise çakışan kümeleri belirtir.
    sil_score = silhouette_score(X_scaled, cluster_labels)
    print("\n--- Model Değerlendirme Sonuçları ---")
    print(f"Seçilen Küme Sayısı (K): {optimal_k}")
    print(f"Küme İçi Hata Kareler Toplamı (Inertia/WCSS): {final_kmeans.inertia_:.4f}")
    print(f"Silhouette Skoru: {sil_score:.4f}")

    # 6. Küme Merkezleri (Centroids)
    # Ölçeklendirilmiş uzaydaki merkezleri orijinal ölçeğe geri döndürüyoruz (Inversing transform)
    centroids = scaler.inverse_transform(final_kmeans.cluster_centers_)
    print("\n--- Orijinal Ölçekteki Küme Merkezleri (Centroids) ---")
    centroids_df = pd.DataFrame(centroids, columns=df_x.columns)
    print(centroids_df)

    # 7. Görselleştirme: Dirsek Yöntemi ve Kümeleme Grafiği
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: Dirsek Yöntemi (Elbow Method)
    axes[0].plot(k_values, inertias, color="blue", marker="o", linestyle="solid", linewidth=2, markersize=8)
    axes[0].axvline(x=optimal_k, color="red", linestyle="--", label=f"Seçilen K ({optimal_k})")
    axes[0].set_xlabel("Küme Sayısı (K Value)")
    axes[0].set_ylabel("Küme İçi Hata Kareler Toplamı (WCSS/Inertia)")
    axes[0].set_title("Optimal K İçin Dirsek Yöntemi")
    axes[0].set_xticks(k_values)
    axes[0].legend()
    axes[0].grid(True)

    # Sağ Grafik: Kümeleme Sonuçları (2 Öznitelik Üzerinden Görselleştirme)
    # Taç yaprak uzunluğu (petal length) ve genişliği (petal width) üzerinden kümelerin dağılımı
    x_col = "petal length (cm)"
    y_col = "petal width (cm)"
    x_idx = df_x.columns.get_loc(x_col)
    y_idx = df_x.columns.get_loc(y_col)

    colors = ["salmon", "lightblue", "lightgreen"]
    for i in range(optimal_k):
        # Her bir kümeye ait veri noktalarını çizdirme
        cluster_data = df_x[cluster_labels == i]
        axes[1].scatter(
            cluster_data[x_col], 
            cluster_data[y_col], 
            color=colors[i], 
            label=f"Küme {i}", 
            alpha=0.8, 
            edgecolors="k"
        )

    # Küme merkezlerini (centroids) büyük kırmızı yıldız olarak grafiğe ekleme
    axes[1].scatter(
        centroids[:, x_idx], 
        centroids[:, y_idx], 
        color="red", 
        marker="*", 
        s=250, 
        label="Küme Merkezleri", 
        edgecolors="black"
    )

    axes[1].set_xlabel(x_col.capitalize())
    axes[1].set_ylabel(y_col.capitalize())
    axes[1].set_title(f"K-Means Kümeleme Sonuçları (K = {optimal_k})")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    output_image = "kmeans_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_kmeans_clustering()