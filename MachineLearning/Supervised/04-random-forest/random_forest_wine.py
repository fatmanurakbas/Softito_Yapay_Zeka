import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)
from sklearn.model_selection import train_test_split


def run_random_forest():
    # 1. Veri Kümesini Yükleme
    # Scikit-learn kütüphanesindeki şarap sınıflandırma (wine) veri seti kullanılmıştır.
    # Bu veri seti, İtalya'nın aynı bölgesinde yetiştirilen üç farklı kültivardan
    # üretilen şarapların kimyasal analiz sonuçlarını (13 öznitelik) içerir.
    # Hedef Değişken (Sınıf): 0, 1, 2 (Üç farklı şarap üreticisi/kültivarı)
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
    # RandomForest bir topluluk (ensemble) modelidir.
    # n_estimators: Ormandaki karar ağacı sayısı.
    # bootstrap: Her ağaç eğitilirken verinin rastgele alt kümelerinin (bootstrap) seçilmesi.
    model = RandomForestClassifier(
        n_estimators=100, max_depth=4, random_state=42, bootstrap=True
    )
    model.fit(X_train, y_train)

    # 4. Tahmin Yapma
    y_pred = model.predict(X_test)

    # 5. Model Değerlendirme Metrikleri
    accuracy = accuracy_score(y_test, y_pred)
    print("\n--- Model Değerlendirme Sonuçları ---")
    print(f"Accuracy (Doğruluk):  {accuracy:.4f}")

    print("\n--- Detaylı Sınıflandırma Raporu ---")
    print(classification_report(y_test, y_pred, target_names=wine.target_names))

    # 6. Öznitelik Önem Dereceleri (Feature Importances)
    # Rastgele orman, tüm ağaçlardaki dallanma kriteri kazançlarını (Gini) 
    # ortalayarak daha kararlı bir öznitelik önem derecesi sunar.
    importance_df = pd.DataFrame(
        {"Öznitelik": df_x.columns, "Önem Derecesi": model.feature_importances_}
    ).sort_values(by="Önem Derecesi", ascending=False)

    print("\n--- Öznitelik Önem Dereceleri (İlk 5) ---")
    print(importance_df.head(5).to_string(index=False))

    # 7. Görselleştirme: Hata Matrisi ve Öznitelik Önem Dereceleri
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: Hata Matrisi (Confusion Matrix)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=wine.target_names)
    disp.plot(ax=axes[0], cmap=plt.cm.Purples, values_format="d")
    axes[0].set_title("Hata Matrisi (Confusion Matrix)")

    # Sağ Grafik: Öznitelik Önem Dereceleri
    # En önemli öznitelikleri görselleştirmek için yatay çubuk grafik çizdirilir.
    importance_df_sorted = importance_df.sort_values(by="Önem Derecesi", ascending=True)
    axes[1].barh(importance_df_sorted["Öznitelik"], importance_df_sorted["Önem Derecesi"], color="purple")
    axes[1].set_xlabel("Gini Önem Derecesi")
    axes[1].set_title("Öznitelik Önem Dereceleri")
    axes[1].grid(axis="x", linestyle="--")

    plt.tight_layout()
    output_image = "random_forest_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_random_forest()