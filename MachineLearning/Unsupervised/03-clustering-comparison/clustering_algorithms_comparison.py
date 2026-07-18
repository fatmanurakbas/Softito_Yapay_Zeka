import os
import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans
from sklearn.datasets import make_circles, make_blobs
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Gereksiz uyarıları engelleme
warnings.filterwarnings("ignore")


def generate_comparison_datasets():
    # 3 farklı geometrik zorluk derecesine sahip yapay veri kümeleri üretme
    np.random.seed(42)
    n_samples = 300

    # 1. İç içe Halkalar (Concentric Circles) - Doğrusal Olmayan Geometri
    X_circles, _ = make_circles(n_samples=n_samples, factor=0.5, noise=0.05, random_state=42)

    # 2. Esnetilmiş/Eğik Elipsler (Anisotropic/Stretched Blobs) - Doğrusal ama eğik geometri
    X_blobs, _ = make_blobs(n_samples=n_samples, random_state=170)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    X_stretched = np.dot(X_blobs, transformation)

    # 3. Farklı Varyanslara Sahip Gruplar (Unequal Variance Blobs)
    X_variances, _ = make_blobs(
        n_samples=n_samples, 
        cluster_std=[1.0, 2.5, 0.5], 
        random_state=42
    )

    return [
        ("İç İçe Halkalar (Circles)", X_circles, 2),
        ("Esnetilmiş Elipsler (Stretched)", X_stretched, 3),
        ("Farklı Varyanslı Gruplar (Variances)", X_variances, 3)
    ]


def run_clustering_comparison():
    datasets = generate_comparison_datasets()

    # Çizim alanı kurulumu: 3 Veri Seti (Satır) x 3 Algoritma (Sütun)
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    
    # Algoritma isimleri (Grafik başlıkları için)
    algo_names = ["K-Means\n(Merkez Tabanlı)", "Agglomerative\n(Hiyerarşik / Bağlantı)", "DBSCAN\n(Yoğunluk Tabanlı)"]

    for row_idx, (data_name, X_raw, n_clusters) in enumerate(datasets):
        # Tüm mesafe tabanlı algoritmalar için özellik ölçeklendirmesi zorunludur
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_raw)

        # Her satır (veri seti) için algoritmaların parametrelerinin tanımlanması
        # DBSCAN parametreleri veri geometrisine göre optimize edilmiştir
        eps_val = 0.25 if "Circles" in data_name else (0.35 if "Stretched" in data_name else 0.4)
        
        models = [
            KMeans(n_clusters=n_clusters, random_state=42, n_init=10),
            AgglomerativeClustering(n_clusters=n_clusters, linkage="ward"),
            DBSCAN(eps=eps_val, min_samples=5)
        ]

        for col_idx, model in enumerate(models):
            # Modeli eğitme ve tahmin etme
            labels = model.fit_predict(X_scaled)

            # Performans ölçümü (Silhouette Skoru)
            # Silhouette skoru hesaplanırken gürültü noktaları (-1) olan DBSCAN için 
            # en az 2 geçerli küme bulunması şartı kontrol edilir.
            unique_labels = np.unique(labels)
            n_unique_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)
            
            sil_str = "N/A"
            if n_unique_clusters > 1:
                # Gürültü olmayan noktalar maskelenir
                non_noise_mask = labels != -1
                if np.sum(non_noise_mask) > 1:
                    score = silhouette_score(X_scaled[non_noise_mask], labels[non_noise_mask])
                    sil_str = f"{score:.3f}"

            # Alt grafiğe çizim yapma
            ax = axes[row_idx, col_idx]
            
            # Küme renkleri ve gürültü ayrımı
            colors = plt.cm.get_cmap("tab10")(np.linspace(0, 1, len(unique_labels)))
            for label, color in zip(unique_labels, colors):
                if label == -1:
                    # Gürültü (Noise) noktaları siyah çarpı işareti olarak çizilir
                    color = "black"
                    marker = "x"
                    size = 40
                else:
                    marker = "o"
                    size = 30
                
                member_mask = (labels == label)
                ax.scatter(
                    X_raw[member_mask, 0], 
                    X_raw[member_mask, 1], 
                    color=color, 
                    marker=marker, 
                    s=size, 
                    edgecolors="k" if label != -1 else None, 
                    alpha=0.7
                )

            # İlk satırdaki grafiklerin tepesine algoritma adını yazma
            if row_idx == 0:
                ax.set_title(algo_names[col_idx], fontsize=13, fontweight="bold")

            # Sol sütundaki grafiklerin yanına veri kümesi adını yazma
            if col_idx == 0:
                ax.set_ylabel(data_name, fontsize=11, fontweight="bold")

            # Grafik içine bilgi kutucuğu ekleme
            info_text = f"Clusters: {n_unique_clusters}\nSil. Score: {sil_str}"
            ax.text(0.05, 0.05, info_text, transform=ax.transAxes, fontsize=9,
                    bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.3'))
            
            ax.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    output_image = "clustering_comparison_grid.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_clustering_comparison()