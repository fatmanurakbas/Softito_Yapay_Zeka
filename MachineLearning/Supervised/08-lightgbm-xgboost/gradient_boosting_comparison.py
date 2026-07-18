import os
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def run_boosting_comparison():
    # 1. Veri Kümesini Yükleme
    # Sınıflandırma yeteneklerini ve hız farkını ölçmek için 30 öznitelikli Breast Cancer veri seti kullanılmıştır.
    cancer = load_breast_cancer(as_frame=True)
    df_x = cancer.data
    df_y = cancer.target

    # 2. Eğitim ve Test Verisi Olarak Ayırma
    X_train, X_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size=0.2, random_state=42, stratify=df_y
    )

    # 3. XGBoost Model Eğitimi ve Süre Ölçümü
    # eval_metric='logloss' uyarısı almamak için açıkça belirtilmiştir.
    xgb_model = XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss",
        verbosity=0,
    )

    start_time = time.time()
    xgb_model.fit(X_train, y_train)
    xgb_train_time = (time.time() - start_time) * 1000  # Milisaniye

    # XGBoost Tahminleri
    y_pred_xgb = xgb_model.predict(X_test)
    y_prob_xgb = xgb_model.predict_proba(X_test)[:, 1]

    # 4. LightGBM Model Eğitimi ve Süre Ölçümü
    # verbose=-1 konsol temizliği için eklenmiştir.
    lgb_model = LGBMClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        verbose=-1,
    )

    start_time = time.time()
    lgb_model.fit(X_train, y_train)
    lgb_train_time = (time.time() - start_time) * 1000  # Milisaniye

    # LightGBM Tahminleri
    y_pred_lgb = lgb_model.predict(X_test)
    y_prob_lgb = lgb_model.predict_proba(X_test)[:, 1]

    # 5. Performans Karşılaştırma Raporu
    comparison_data = {
        "Metrik": ["Eğitim Süresi (ms)", "Doğruluk (Accuracy)", "F1-Score", "ROC-AUC"],
        "XGBoost": [
            f"{xgb_train_time:.2f} ms",
            f"{accuracy_score(y_test, y_pred_xgb):.4f}",
            f"{f1_score(y_test, y_pred_xgb):.4f}",
            f"{roc_auc_score(y_test, y_prob_xgb):.4f}",
        ],
        "LightGBM": [
            f"{lgb_train_time:.2f} ms",
            f"{accuracy_score(y_test, y_pred_lgb):.4f}",
            f"{f1_score(y_test, y_pred_lgb):.4f}",
            f"{roc_auc_score(y_test, y_prob_lgb):.4f}",
        ],
    }
    comparison_df = pd.DataFrame(comparison_data)

    print("--- Model Performans Karşılaştırma Raporu ---")
    print(comparison_df.to_string(index=False))

    # 6. Görselleştirme: ROC Eğrileri ve Öznitelik Önem Dereceleri
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: ROC Eğrileri Karşılaştırması
    fpr_xgb, tpr_xgb, _ = roc_curve(y_test, y_prob_xgb)
    fpr_lgb, tpr_lgb, _ = roc_curve(y_test, y_prob_lgb)

    axes[0].plot(
        fpr_xgb,
        tpr_xgb,
        color="darkblue",
        lw=2,
        label=f"XGBoost (AUC = {roc_auc_score(y_test, y_prob_xgb):.4f})",
    )
    axes[0].plot(
        fpr_lgb,
        tpr_lgb,
        color="darkorange",
        lw=2,
        label=f"LightGBM (AUC = {roc_auc_score(y_test, y_prob_lgb):.4f})",
    )
    axes[0].plot([0, 1], [0, 1], color="gray", linestyle="--")
    axes[0].set_xlim([0.0, 1.0])
    axes[0].set_ylim([0.0, 1.05])
    axes[0].set_xlabel("Yanlış Pozitif Oranı (FPR)")
    axes[0].set_ylabel("Doğru Pozitif Oranı (TPR)")
    axes[0].set_title("ROC Eğrileri Karşılaştırması")
    axes[0].legend(loc="lower right")
    axes[0].grid(True)

    # Sağ Grafik: Öznitelik Önem Dereceleri Karşılaştırması (İlk 10 Öznitelik)
    # XGBoost ve LightGBM öznitelik önemlerini yan yana inceleyelim
    xgb_importances = pd.Series(xgb_model.feature_importances_, index=df_x.columns)
    lgb_importances = pd.Series(lgb_model.feature_importances_, index=df_x.columns)

    # Normalleştirme (0-1 aralığına çekerek adil kıyaslama)
    xgb_importances = xgb_importances / xgb_importances.sum()
    lgb_importances = lgb_importances / lgb_importances.sum()

    importance_compare = pd.DataFrame(
        {"XGBoost": xgb_importances, "LightGBM": lgb_importances}
    )
    # En yüksek ortalama öneme sahip ilk 10 özniteliği alalım
    importance_compare["Ortalama"] = importance_compare.mean(axis=1)
    top_10_features = (
        importance_compare.sort_values(by="Ortalama", ascending=True)
        .tail(10)
        .index
    )

    importance_compare.loc[top_10_features, ["XGBoost", "LightGBM"]].plot(
        kind="barh", ax=axes[1], color=["darkblue", "orange"]
    )
    axes[1].set_title("Öznitelik Önem Derecesi Karşılaştırması (Top 10)")
    axes[1].set_xlabel("Normalize Edilmiş Önem Skoru")
    axes[1].grid(axis="x", linestyle="--")

    plt.tight_layout()
    output_image = "boosting_comparison_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_boosting_comparison()