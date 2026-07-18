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
from sklearn.tree import DecisionTreeClassifier, plot_tree


def run_decision_tree():
    # 1. Veri Kümesini Yükleme
    # Scikit-learn kütüphanesindeki klasik Iris çiçek veri seti kullanılmıştır.
    # Bu veri seti 3 farklı çiçek türüne (Setosa, Versicolor, Virginica) ait
    # 150 adet örneğin çanak ve taç yaprak uzunluk/genişlik ölçümlerini içerir.
    iris = load_iris(as_frame=True)
    df_x = iris.data
    df_y = iris.target

    print("--- Veri Kümesi Özeti ---")
    print(f"Öznitelik Sayısı: {df_x.shape[1]}")
    print(f"Örnek Sayısı: {df_x.shape[0]}")
    print(f"Sınıf Dağılımı (Çiçek Sınıfları):")
    print(df_y.value_counts().rename({0: "Setosa", 1: "Versicolor", 2: "Virginica"}))

    # 2. Eğitim ve Test Verisi Olarak Ayırma
    X_train, X_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size=0.2, random_state=42, stratify=df_y
    )

    # 3. Model Kurulumu ve Eğitimi
    # Karar ağacının aşırı öğrenmesini (overfitting) engellemek amacıyla max_depth
    # parametresi sınırlandırılmıştır. splitting kriteri olarak Gini katsayısı seçilmiştir.
    # Karar ağaçları, ölçeklendirmeden (feature scaling) etkilenmez.
    model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
    model.fit(X_train, y_train)

    # 4. Tahmin Yapma
    y_pred = model.predict(X_test)

    # 5. Model Değerlendirme Metrikleri
    # Çoklu sınıflandırma (multi-class) olduğu için metrikler ağırlıklı ortalama ile incelenir.
    accuracy = accuracy_score(y_test, y_pred)
    print("\n--- Model Değerlendirme Sonuçları ---")
    print(f"Accuracy (Doğruluk):  {accuracy:.4f}")

    print("\n--- Detaylı Sınıflandırma Raporu ---")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # 6. Öznitelik Önem Dereceleri (Feature Importances)
    # Karar ağaçları, hangi özniteliğin kararlarda ne kadar pay sahibi olduğunu hesaplayabilir.
    importance_df = pd.DataFrame(
        {"Öznitelik": df_x.columns, "Önem Derecesi": model.feature_importances_}
    ).sort_values(by="Önem Derecesi", ascending=False)

    print("\n--- Öznitelik Önem Dereceleri ---")
    print(importance_df.to_string(index=False))

    # 7. Görselleştirme: Hata Matrisi ve Karar Ağacı Yapısı
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # Sol Grafik: Hata Matrisi (Confusion Matrix)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
    disp.plot(ax=axes[0], cmap=plt.cm.Greens, values_format="d")
    axes[0].set_title("Hata Matrisi (Confusion Matrix)")

    # Sağ Grafik: Karar Ağacı Yapısı (Decision Tree structure)
    # plot_tree fonksiyonu ile ağacın kuralları nasıl böldüğü çizdirilir.
    plot_tree(
        model,
        feature_names=iris.feature_names,
        class_names=iris.target_names,
        filled=True,
        ax=axes[1],
        rounded=True,
    )
    axes[1].set_title("Eğitilen Karar Ağacı Yapısı")

    plt.tight_layout()
    output_image = "decision_tree_structure.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_decision_tree()