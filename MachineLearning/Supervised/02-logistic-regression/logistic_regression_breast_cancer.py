import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def run_logistic_regression():
    # 1. Veri Kümesini Yükleme
    # Scikit-learn kütüphanesindeki hazır meme kanseri (breast cancer) veri seti kullanılmıştır.
    # Bu veri seti 569 hastaya ait tümör hücrelerinin 30 farklı geometrik özelliğini içerir.
    # Hedef Değişken (Target): 0 = Malignant (Kötü Huylu), 1 = Benign (İyi Huylu)
    cancer = load_breast_cancer(as_frame=True)
    df_x = cancer.data
    df_y = cancer.target

    print("--- Veri Kümesi Özeti ---")
    print(f"Öznitelik Sayısı: {df_x.shape[1]}")
    print(f"Örnek Sayısı: {df_x.shape[0]}")
    print(f"Sınıf Dağılımı:")
    print(df_y.value_counts().rename({0: "Malignant (0)", 1: "Benign (1)"}))

    # 2. Eğitim ve Test Verisi Olarak Ayırma
    # Sınıf dengesizliği riskine karşı 'stratify' parametresi kullanılarak bölünmüştür.
    X_train, X_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size=0.2, random_state=42, stratify=df_y
    )

    # 3. Öznitelik Ölçeklendirme (Feature Scaling)
    # Lojistik Regresyon gibi gradyan tabanlı ve düzenlileştirme (regularization) kullanan
    # modellerde girdilerin standartlaştırılması (Z-skoru ölçeklendirmesi) kararlılık için önemlidir.
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Model Kurulumu ve Eğitimi
    # max_iter parametresi modelin yakınsaması (convergence) için artırılmıştır.
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train_scaled, y_train)

    # 5. Tahmin Yapma
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]  # Pozitif sınıf (1) olasılıkları

    # 6. Model Değerlendirme Metrikleri
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    print("\n--- Model Değerlendirme Sonuçları ---")
    print(f"Accuracy (Doğruluk):  {accuracy:.4f}")
    print(f"Precision (Kesinlik): {precision:.4f}")
    print(f"Recall (Duyarlılık):  {recall:.4f}")
    print(f"F1-Score:             {f1:.4f}")
    print(f"ROC-AUC Skoru:        {roc_auc:.4f}")

    print("\n--- Detaylı Sınıflandırma Raporu ---")
    print(
        classification_report(
            y_test, y_pred, target_names=["Malignant (0)", "Benign (1)"]
        )
    )

    # 7. Model Parametreleri (Katsayı Analizi)
    # Katsayıların mutlak büyüklüğü, ilgili özniteliğin karara olan etkisini temsil eder.
    importance_df = pd.DataFrame(
        {"Öznitelik": df_x.columns, "Katsayı (Beta)": model.coef_[0]}
    )
    importance_df["Mutlak_Katsayı"] = importance_df["Katsayı (Beta)"].abs()
    importance_df = importance_df.sort_values(by="Mutlak_Katsayı", ascending=False).head(10)

    print("\n--- En Etkili 10 Öznitelik (Katsayı Analizi) ---")
    print(importance_df[["Öznitelik", "Katsayı (Beta)"]].to_string(index=False))

    # 8. Görselleştirme: Hata Matrisi ve ROC Eğrisi
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Sol Grafik: Hata Matrisi (Confusion Matrix)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Malignant", "Benign"])
    disp.plot(ax=axes[0], cmap=plt.cm.Blues, values_format="d")
    axes[0].set_title("Hata Matrisi (Confusion Matrix)")

    # Sağ Grafik: ROC Eğrisi (Receiver Operating Characteristic)
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    axes[1].plot(fpr, tpr, color="darkorange", lw=2, label=f"ROC Eğrisi (Alan = {roc_auc:.4f})")
    axes[1].plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
    axes[1].set_xlim([0.0, 1.0])
    axes[1].set_ylim([0.0, 1.05])
    axes[1].set_xlabel("Yanlış Pozitif Oranı (FPR)")
    axes[1].set_ylabel("Doğru Pozitif Oranı (TPR)")
    axes[1].set_title("ROC Eğrisi (ROC Curve)")
    axes[1].legend(loc="lower right")
    axes[1].grid(True)

    plt.tight_layout()
    output_image = "logistic_regression_metrics.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_logistic_regression()