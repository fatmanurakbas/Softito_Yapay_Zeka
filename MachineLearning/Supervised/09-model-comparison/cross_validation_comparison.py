import os
import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

# Uyarıları kapatma (Gereksiz konsol kirliliğini önlemek için)
warnings.filterwarnings("ignore")


def run_model_comparison():
    # 1. Veri Kümesini Yükleme
    # 8 farklı modeli eşit şartlarda yarıştırmak için Breast Cancer veri kümesi kullanılmıştır.
    cancer = load_breast_cancer(as_frame=True)
    df_x = cancer.data
    df_y = cancer.target

    # 2. Öznitelik Ölçeklendirme (Feature Scaling)
    # KNN, SVM ve Lojistik Regresyon gibi mesafe ve gradyan tabanlı modeller ölçeklendirmeye ihtiyaç duyar.
    # Ağaç ve olasılık tabanlı modeller ölçeklendirmeden zarar görmez. Bu yüzden veriyi toplu standartlaştırıyoruz.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_x)

    # 3. Yarışacak Modellerin Tanımlanması
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42),
        "SVM (RBF)": SVC(kernel="rbf", C=1.0, probability=True, random_state=42),
        "KNN (K=5)": KNeighborsClassifier(n_neighbors=5),
        "Gaussian NB": GaussianNB(),
        "XGBoost": XGBClassifier(n_estimators=100, max_depth=4, eval_metric="logloss", verbosity=0, random_state=42),
        "LightGBM": LGBMClassifier(n_estimators=100, max_depth=4, verbose=-1, random_state=42),
    }

    # 4. Çapraz Doğrulama Kurulumu (Stratified 5-Fold)
    # Sınıf dağılım oranlarını her katlamada (fold) eşit korumak için StratifiedKFold tercih edilmiştir.
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    results = {}
    print("--- Modeller Çapraz Doğrulama (Cross-Validation) Sürecinde ---")
    
    for name, model in models.items():
        # Her model için 5 farklı katlamadaki doğruluk (accuracy) skorları hesaplanır
        scores = cross_val_score(model, X_scaled, df_y, cv=cv, scoring="accuracy")
        results[name] = scores
        print(f"[{name}] eğitildi. Ortalama Doğruluk: {scores.mean():.4f}")

    # 5. Sonuçların Tablolaştırılması
    # Modellerin ortalama doğruluğu ve varyansı (standart sapması) hesaplanarak sıralanır.
    summary_data = []
    for name, scores in results.items():
        summary_data.append({
            "Model": name,
            "Ortalama Doğruluk (Mean Accuracy)": scores.mean(),
            "Standart Sapma (Std Dev)": scores.std()
        })
    
    summary_df = pd.DataFrame(summary_data).sort_values(
        by="Ortalama Doğruluk (Mean Accuracy)", ascending=False
    )

    print("\n--- Çapraz Doğrulama Sıralama Raporu ---")
    print(summary_df.to_string(index=False))

    # 6. Görselleştirme: Kutu Grafiği (Box Plot) İle Performans Dağılımları
    # Sadece ortalama başarıya bakmak yetmez; modelin ne kadar kararlı olduğunu (varyansını) görmek gerekir.
    plt.figure(figsize=(12, 6))
    
    # Skorları boxplot ile çizdirme
    plt.boxplot(results.values(), labels=results.keys(), patch_artist=True,
                boxprops=dict(facecolor="lightblue", color="blue"),
                medianprops=dict(color="red", linewidth=2))
    
    plt.ylabel("Çapraz Doğruluk Oranı (Accuracy)")
    plt.title("Sınıflandırma Modelleri Karşılaştırması (5-Fold Cross-Validation)")
    plt.xticks(rotation=30, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    plt.tight_layout()
    output_image = "model_comparison_results.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_model_comparison()