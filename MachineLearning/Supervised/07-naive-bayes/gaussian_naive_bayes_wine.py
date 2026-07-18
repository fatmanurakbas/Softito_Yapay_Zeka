import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.datasets import load_wine
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def run_naive_bayes():
    # 1. Veri Kümesini Yükleme
    # Kimyasal bileşenleri sürekli sayısal değişkenlerden oluşan Wine veri kümesi,
    # özniteliklerin normal dağılım göstermesini bekleyen GaussianNB için idealdir.
    # Hedef Değişken (Sınıf): 0, 1, 2 (Üç farklı şarap sınıfı)
    wine = load_wine(as_frame=True)
    df_x = wine.data
    df_y = wine.target

    print("--- Veri Kümesi Özeti ---")
    print(f"Öznitelik Sayısı: {df_x.shape[1]}")
    print(f"Örnek Sayısı: {df_x.shape[0]}")
    print(f"Sınıf Dağılımı:")
    print(df_y.value_counts().rename({0: "Sınıf 0", 1: "Sınıf 1", 2: "Sınıf 2"}))

    # 2. Eğitim ve Test Verisi Olarak Ayırma
    X_train, X_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size=0.2, random_state=42, stratify=df_y
    )

    # 3. Model Kurulumu ve Eğitimi
    # Naive Bayes ölçeklendirmeden bağımsızdır, her bir özniteliğin sınıflara göre
    # ayrı ayrı ortalamasını ve varyansını çıkarır. Ölçeklendirme (Scaling) gerekmez.
    model = GaussianNB()
    model.fit(X_train, y_train)

    # 4. Tahmin Yapma
    y_pred = model.predict(X_test)

    # 5. Model Değerlendirme Metrikleri
    accuracy = accuracy_score(y_test, y_pred)
    print("\n--- Model Değerlendirme Sonuçları ---")
    print(f"Accuracy (Doğruluk):  {accuracy:.4f}")

    print("\n--- Detaylı Sınıflandırma Raporu ---")
    print(classification_report(y_test, y_pred, target_names=wine.target_names))

    # 6. Naive Bayes İstatistikleri (Sınıf Ortalama ve Varyansları)
    # Modelin her bir öznitelik için hesapladığı sınıf bazlı ortalamalar (Means)
    feature_name = "alcohol"
    feature_idx = df_x.columns.get_loc(feature_name)
    print(f"\n--- '{feature_name.upper()}' Özniteliği İçin Hesaplanan Sınıf Ortalamaları ---")
    for i, class_name in enumerate(wine.target_names):
        mean_val = model.theta_[i, feature_idx]  # theta_: Ortalama değer matrisi
        var_val = model.var_[i, feature_idx]    # var_: Varyans matrisi
        print(f"{class_name}: Ortalama = {mean_val:.4f}, Varyans = {var_val:.4f}")

    # 7. Görselleştirme: Hata Matrisi ve Normal Dağılım Eğrileri (Gaussian PDFs)
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: Hata Matrisi (Confusion Matrix)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=wine.target_names)
    disp.plot(ax=axes[0], cmap=plt.cm.YlOrBr, values_format="d")
    axes[0].set_title("Hata Matrisi (Confusion Matrix)")

    # Sağ Grafik: Sınıflara Göre 'Alcohol' Özniteliğinin Gaussian Dağılım Eğrileri
    # Bu grafik, Naive Bayes'in sınıfları nasıl ayırt etmek için olasılık yoğunluk fonksiyonu çizdiğini gösterir.
    colors = ["red", "blue", "green"]
    for i, class_name in enumerate(wine.target_names):
        mean = model.theta_[i, feature_idx]
        std = np.sqrt(model.var_[i, feature_idx])
        
        # Sınıfa özel x ekseni aralığı oluşturma ve Normal Olasılık Yoğunluk Fonksiyonu (PDF) çizimi
        x_axis = np.linspace(df_x[feature_name].min(), df_x[feature_name].max(), 100)
        axes[1].plot(x_axis, norm.pdf(x_axis, mean, std), label=f"{class_name} (PDF)", color=colors[i], lw=2)
        
        # Eğitilen verinin gerçek dağılım noktalarını göstermek için küçük çizgiler (rug plot)
        class_samples = X_train[y_train == i][feature_name]
        axes[1].plot(class_samples, np.zeros_like(class_samples) - 0.05, '|', color=colors[i], markersize=10, alpha=0.5)

    axes[1].set_xlabel(f"{feature_name.capitalize()} Değeri")
    axes[1].set_ylabel("Olasılık Yoğunluğu (Probability Density)")
    axes[1].set_title(f"Sınıf Bazlı '{feature_name.capitalize()}' Dağılımı")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    output_image = "naive_bayes_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_naive_bayes()