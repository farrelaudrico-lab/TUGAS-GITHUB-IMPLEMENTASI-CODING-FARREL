import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def main():
    rng = np.random.default_rng(7)
    n = 600
    # Fitur sintetis yang menyerupai indikator yang mungkin dianalisis.
    perubahan_ndvi = rng.uniform(-0.8, 0.2, n)      # penurunan vegetasi cenderung negatif
    perubahan_nbr = rng.uniform(-0.7, 0.3, n)       # perubahan terkait area terbakar/vegetasi
    jarak_jalan_km = rng.uniform(0, 20, n)
    curah_hujan_mm = rng.uniform(20, 350, n)

    labels = []
    for ndvi, nbr, jalan, hujan in zip(perubahan_ndvi, perubahan_nbr, jarak_jalan_km, curah_hujan_mm):
        if nbr < -0.42 and hujan < 180:
            labels.append("indikasi kebakaran (simulasi)")
        elif jalan < 3.5 and ndvi < -0.35:
            labels.append("indikasi pembukaan dekat jalan (simulasi)")
        else:
            labels.append("perubahan lain/tidak pasti (simulasi)")

    df = pd.DataFrame({
        "perubahan_ndvi": perubahan_ndvi,
        "perubahan_nbr": perubahan_nbr,
        "jarak_jalan_km": jarak_jalan_km,
        "curah_hujan_mm": curah_hujan_mm,
        "label_simulasi": labels
    })
    X = df[["perubahan_ndvi", "perubahan_nbr", "jarak_jalan_km", "curah_hujan_mm"]]
    y = df["label_simulasi"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=160, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("=== KLASIFIKASI PERUBAHAN TUTUPAN LAHAN (DATA SINTETIS) ===")
    print(f"Jumlah sampel: {len(df)}")
    print(f"Akurasi uji  : {accuracy_score(y_test, pred):.3f}")
    print("\nLaporan klasifikasi:")
    print(classification_report(y_test, pred, zero_division=0))
    print("Fitur penting:")
    print(pd.Series(model.feature_importances_, index=X.columns)
            .sort_values(ascending=False).to_string())

    contoh = pd.DataFrame([{
        "perubahan_ndvi": -0.52,
        "perubahan_nbr": -0.55,
        "jarak_jalan_km": 2.0,
        "curah_hujan_mm": 90
    }])
    print("\nContoh fitur baru:")
    print(contoh.to_string(index=False))
    print("Kelas prediksi:", model.predict(contoh)[0])
    print("\nPERINGATAN: label dan fitur adalah simulasi. Prediksi bukan bukti penyebab deforestasi.")

if __name__ == "__main__":
    main()
