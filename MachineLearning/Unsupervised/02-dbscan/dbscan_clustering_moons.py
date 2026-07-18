import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from sklearn.datasets import make_moons
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def run_dbscan_clustering():
    # 1. Doğrusal Olmayan Veri Kümesi Üretme (Moons Dataset)
    # K-Means'in neden yetersiz kaldığını ve DBSCAN'in neden güçlü olduğunu göstermek
    # amacıyla birbirine geçmiş iki hilal şeklinde veri üretilmiştir.
    X_raw, y_true = make_moons(n_samples=300, noise=0.07, random_state=42)
    
    print("--- Veri Kümesi Özeti ---")
    print(f"Örnek Sayısı: {X_raw.shape[0]}")
    print(f"Öznitelik Sayısı: {X_raw.shape[1]}")

    # 2. Öznitelik Ölçeklendirme (Feature Scaling)
    # DBSCAN, epsilon (eps) komşuluk yarıçapını Öklid mesafesi üzerinden hesaplar.
    # Bu nedenle verilerin standartlaştırılması algoritmanın başarısı için zorunludur.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_raw)

    # 3. K-Means Referans Modeli Kurulumu ve Eğitimi
    # Karşılaştırma amacıyla hilal verisinde K-Means eğitilir.
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X_scaled)

    # 4. DBSCAN Model Kurulumu ve Eğitimi
    # eps: Komşuluk yarıçapı.
    # min_samples: Bir noktanın "çekirdek nokta" olabilmesi için yarıçapı içindeki minimum nokta sayısı.
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    dbscan_labels = dbscan.fit_predict(X_scaled)

    # 5. DBSCAN Sonuçlarının Analizi
    # DBSCAN gürültü/aykırı değer olarak saptadığı noktaları -1 olarak etiketler.
    unique_labels = set(dbscan_labels)
    n_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)
    n_noise = list(dbscan_labels).count(-1)

    print("\n--- DBSCAN Kümeleme Analizi ---")
    print(f"Tespit Edilen Küme Sayısı: {n_clusters}")
    print(f"Gürültü (Aykırı Değer) Noktası Sayısı: {n_noise} (Toplam {len(X_scaled)} nokta içinden)")

    if n_clusters > 1:
        # Silhouette skoru sadece gürültü olmayan noktalar üzerinden hesaplanabilir
        non_noise_mask = dbscan_labels != -1
        if np.sum(non_noise_mask) > 1:
            sil_score = silhouette_score(X_scaled[non_noise_mask], dbscan_labels[non_noise_mask])
            print(f"Gürültüsüz Veriler İçin Silhouette Skoru: {sil_score:.4f}")

    # 6. Görselleştirme: K-Means vs. DBSCAN Karşılaştırması
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: K-Means Kümeleme Sonuçları (Doğrusal Kesim)
    # K-Means merkez tabanlı olduğu için hilal şeklindeki kıvrımları ayıramaz, düz bir çizgiyle böler.
    scatter_km = axes[0].scatter(X_raw[:, 0], X_raw[:, 1], c=kmeans_labels, cmap="coolwarm", edgecolors="k", alpha=0.8)
    axes[0].set_title("K-Means Kümeleme (Doğrusal Olmayan Veride Başarısız)")
    axes[0].set_xlabel("Öznitelik 1")
    axes[0].set_ylabel("Öznitelik 2")
    axes[0].grid(True)

    # Sağ Grafik: DBSCAN Kümeleme Sonuçları (Yoğunluk Tabanlı)
    # Gürültü noktalarını ayırt etmek için renk haritasına özel bir mantık ekliyoruz.
    unique_db_labels = np.unique(dbscan_labels)
    colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_db_labels)))

    for label, col in zip(unique_db_labels, colors):
        if label == -1:
            # Gürültü (Noise) noktalarını siyah renkte ve farklı bir sembolle (x) gösteriyoruz
            col = [0, 0, 0, 1]  # Siyah
            marker = "x"
            label_name = "Gürültü / Aykırı Değer"
            size = 50
        else:
            marker = "o"
            label_name = f"Küme {label}"
            size = 40

        class_member_mask = (dbscan_labels == label)
        axes[1].scatter(
            X_raw[class_member_mask, 0],
            X_raw[class_member_mask, 1],
            color=tuple(col),
            marker=marker,
            edgecolors="k" if label != -1 else None,
            s=size,
            label=label_name,
            alpha=0.8
        )

    axes[1].set_title("DBSCAN Kümeleme (Yoğunluk Tabanlı Doğal Bölünme)")
    axes[1].set_xlabel("Öznitelik 1")
    axes[1].set_ylabel("Öznitelik 2")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    output_image = "dbscan_vs_kmeans.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_dbscan_clustering()