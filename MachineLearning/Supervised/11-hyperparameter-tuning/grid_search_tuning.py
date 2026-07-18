import os
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split


def run_hyperparameter_tuning():
    # 1. Veri Kümesini Yükleme
    cancer = load_breast_cancer(as_frame=True)
    df_x = cancer.data
    df_y = cancer.target

    # 2. Eğitim ve Test Verisi Olarak Ayırma
    X_train, X_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size=0.2, random_state=42, stratify=df_y
    )

    # 3. Temel (Baseline - Ayarlanmamış) Model Kurulumu
    # Hiçbir parametre ayarı yapılmadan varsayılan değerlerle eğitilen model
    baseline_model = RandomForestClassifier(random_state=42)
    
    start_time = time.time()
    baseline_model.fit(X_train, y_train)
    baseline_time = (time.time() - start_time) * 1000  # ms
    
    y_pred_base = baseline_model.predict(X_test)
    baseline_acc = accuracy_score(y_test, y_pred_base)

    # 4. Hiperparametre Uzayının (Grid) Tanımlanması
    # Random Forest modeli için taranacak parametreler
    param_grid = {
        "n_estimators": [50, 100, 150, 200],
        "max_depth": [3, 5, 8, None],
        "min_samples_split": [2, 5, 10],
        "criterion": ["gini", "entropy"]
    }
    # Toplam kombinasyon sayısı: 4 * 4 * 3 * 2 = 96 kombinasyon. 
    # 5-Katlı çapraz doğrulama ile toplamda 96 * 5 = 480 model eğitilecektir.

    # 5. Grid Search ile Optimizasyon (Tüm kombinasyonları tarar)
    grid_search = GridSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_grid=param_grid,
        cv=5,
        scoring="accuracy",
        n_jobs=-1  # Tüm işlemci çekirdeklerini kullanır
    )
    
    start_time = time.time()
    grid_search.fit(X_train, y_train)
    grid_time = (time.time() - start_time) * 1000  # ms
    
    # En iyi parametreler ile test kümesinde tahmin yapma
    best_grid_model = grid_search.best_estimator_
    y_pred_grid = best_grid_model.predict(X_test)
    grid_acc = accuracy_score(y_test, y_pred_grid)

    # 6. Random Search ile Optimizasyon (Rastgele kombinasyonları örnekler)
    # n_iter=15 ile 96 kombinasyondan sadece rastgele seçilen 15 tanesi test edilecektir.
    random_search = RandomizedSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_distributions=param_grid,
        n_iter=15,
        cv=5,
        scoring="accuracy",
        random_state=42,
        n_jobs=-1
    )
    
    start_time = time.time()
    random_search.fit(X_train, y_train)
    random_time = (time.time() - start_time) * 1000  # ms
    
    # En iyi parametreler ile test kümesinde tahmin yapma
    best_random_model = random_search.best_estimator_
    y_pred_random = best_random_model.predict(X_test)
    random_acc = accuracy_score(y_test, y_pred_random)

    # 7. Sonuçların Karşılaştırılması
    results_data = {
        "Yöntem": ["Baseline (Varsayılan)", "Grid Search (96 Kombinasyon)", "Random Search (15 Kombinasyon)"],
        "Süre (Milisaniye)": [f"{baseline_time:.2f} ms", f"{grid_time:.2f} ms", f"{random_time:.2f} ms"],
        "Test Doğruluğu (Accuracy)": [f"{baseline_acc:.4f}", f"{grid_acc:.4f}", f"{random_acc:.4f}"]
    }
    results_df = pd.DataFrame(results_data)
    
    print("--- Hiperparametre Optimizasyonu Kıyaslama Raporu ---")
    print(results_df.to_string(index=False))
    
    print("\n--- Grid Search En İyi Parametreler ---")
    print(grid_search.best_params_)
    
    print("\n--- Random Search En İyi Parametreler ---")
    print(random_search.best_params_)

    # 8. Görselleştirme: Doğruluk vs Arama Süreleri
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Sol Grafik: Doğruluk Skorları Kıyası
    methods = ["Baseline", "Grid Search", "Random Search"]
    accuracies = [baseline_acc, grid_acc, random_acc]
    axes[0].bar(methods, accuracies, color=["gray", "darkblue", "teal"], width=0.5)
    axes[0].set_ylabel("Test Doğruluğu (Accuracy)")
    axes[0].set_ylim([0.90, 1.0])  # Detayları daha rahat görmek için alt limit ayarlanmıştır
    axes[0].set_title("Modellerin Test Doğruluğu Karşılaştırması")
    for i, v in enumerate(accuracies):
        axes[0].text(i, v + 0.002, f"{v:.4f}", ha="center", fontweight="bold")

    # Sağ Grafik: Optimizasyon Süreleri Kıyası
    times = [baseline_time, grid_time, random_time]
    axes[1].bar(methods, times, color=["gray", "darkblue", "teal"], width=0.5)
    axes[1].set_ylabel("Süre (Milisaniye)")
    axes[1].set_title("Arama ve Eğitim Süreleri Karşılaştırması")
    for i, v in enumerate(times):
        axes[1].text(i, v + (max(times)*0.02), f"{v:.1f} ms", ha="center", fontweight="bold")

    plt.tight_layout()
    output_image = "hyperparameter_tuning_comparison.png"
    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"\nGörselleştirme grafiği başarıyla kaydedildi: {output_image}")


if __name__ == "__main__":
    run_hyperparameter_tuning()