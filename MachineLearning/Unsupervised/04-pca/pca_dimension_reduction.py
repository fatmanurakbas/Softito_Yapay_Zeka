import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def run_pca_dimension_reduction():
    # 1. Veri Kümesini Yükleme
    # 30 boyutlu (öznitelikli) Breast Cancer veri kümesi, boyut azaltmanın gücünü göstermek için idealdir.
    cancer = load_breast_cancer(as_frame=True)
    df_x = cancer.data
    df_y = cancer.target

    print("--- Veri Kümesi Özeti ---")
    print(f"Orijinal Öznitelik Boyutu (Sütun Sayısı): {df_x.shape[1]}")
    print(f"Örnek Sayısı: {df_x.shape[0]}")

    # 2. Öznitelik Ölçeklendirme (Feature Scaling)
    # PCA, özniteliklerin varyanslarını maksimize etmeye odaklanır.
    # Büyük aralıklı özniteliklerin analiz sonucunu bozmaması için standartlaştırma ŞARTTIR.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_x)

    # 3. Kümülatif Varyans Analizi (Scree Analizi)
    # Kaç temel bileşenin orijinal veriyi ne oranda temsil ettiğini görmek için tüm boyutlar (30) eğitilir.
    pca_full = PCA(random_state=42)
    pca_full.fit(X_scaled)
    
    # Her bir bileşenin açıkladığı varyans oranı (Explained Variance Ratio)
    explained_variance = pca_full.explained_variance_ratio_
    cumulative_variance = np.cumsum(explained_variance)

    # %90 bilgi koruma sınırına kaç bileşenle ulaştığımızı hesaplama
    components_90 = np.argmax(cumulative_variance >= 0.90) + 1
    print("\n--- Varyans Analiz Sonuçları ---")
    print(f"İlk 2 bileşenin koruduğu toplam bilgi oranı: {cumulative_variance[1]*100:.2f}%")
    print(f"Orijinal verinin %90 bilgisini korumak için gereken minimum bileşen sayısı: {components_90}")

    # 4. 2 Boyuta İndirgeme (PCA to 2D Project)
    # Veriyi görselleştirebilmek amacıyla en yüksek varyansa sahip ilk 2 temel bileşene indirgiyoruz.
    pca_2d = PCA(n_components=2, random_state=42)
    X_pca = pca_2d.fit_transform(X_scaled)

    # Elde edilen yeni 2 boyutlu veriyi DataFrame'e dönüştürme
    pca_df = pd.DataFrame(data=X_pca, columns=["PC1", "PC2"])
    pca_df["target"] = df_y.values

    # 5. Görselleştirme: Kümülatif Varyans Grafiği ve 2D Sınıf Dağılımı
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: Kümülatif Açıklanan Varyans Eğrisi (Scree Plot)
    axes[0].plot(range(1, 31), cumulative_variance, color="blue", marker="o", linestyle="-", linewidth=2)
    axes[0].axhline(y=0.90, color="red", linestyle="--", label="90% Bilgi Sınırı (Threshold)")
    axes[0].axvline(x=components_90, color="red", linestyle="--")
    axes[0].set_xlabel("Temel Bileşen Sayısı (Number of Components)")
    axes[0].set_ylabel("Kümülatif Açıklanan Varyans Oranı (Cumulative Variance)")
    axes[0].set_title("Boyut Analizi: Açıklanan Varyans Eğrisi")
    axes[0].grid(True)
    axes[0].legend()

    # Sağ Grafik: 2D PCA İzdüşümü (PC1 vs PC2)
    # 30 boyuttaki karmaşık verinin 2 boyutta nasıl kümelendiğini ve ayrıştığını inceliyoruz.
    targets = [0, 1]
    colors = ["salmon", "lightblue"]
    labels = ["Malignant (Kötü Huylu)", "Benign (İyi Huylu)"]

    for target, color, label in zip(targets, colors, labels):
        indices_to_keep = pca_df["target"] == target
        axes[1].scatter(
            pca_df.loc[indices_to_keep, "PC1"],
            pca_df.loc[indices_to_keep, "PC2"],
            color=color,
            label=label,
            edgecolors="k",
            alpha=0.8,
            s=40
        )

    axes[1].set_xlabel(f"Temel Bileşen 1 (PC1 - {explained_variance[0]*100:.1f}%)")
    axes[1].set_ylabel(f"Temel Bileşen 2 (PC2 - {explained_variance[1]*100:.1f}%)")
    axes[1].set_title("30 Boyuttan 2 Boyuta PCA İzdüşümü")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    output_image = "pca_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_pca_dimension_reduction()