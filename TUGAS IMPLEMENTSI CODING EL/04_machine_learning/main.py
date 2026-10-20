import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    rng = np.random.default_rng(42)
    n = 500
    jam_belajar = rng.uniform(0, 10, n)
    kehadiran = rng.uniform(40, 100, n)
    tugas_selesai = rng.integers(0, 11, n)

    # Label sintetis dengan sedikit noise agar contoh lebih realistis.
    skor = 0.45 * jam_belajar + 0.035 * kehadiran + 0.35 * tugas_selesai
    noise = rng.normal(0, 0.6, n)
    lulus = ((skor + noise) >= 5.7).astype(int)

    X = np.column_stack([jam_belajar, kehadiran, tugas_selesai])
    y = lulus
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)
    prediksi = model.predict(X_test)

    print("=== KLASIFIKASI KELULUSAN KURSUS ===")
    print(f"Jumlah data       : {n}")
    print(f"Akurasi data uji  : {accuracy_score(y_test, prediksi):.3f}")
    print("\nLaporan klasifikasi:")
    print(classification_report(y_test, prediksi, target_names=["Belum Lulus", "Lulus"], zero_division=0))
    print("Confusion matrix (baris=label asli, kolom=prediksi):")
    print(confusion_matrix(y_test, prediksi))

    peserta_baru = np.array([[6.5, 90, 8]])
    hasil = model.predict(peserta_baru)[0]
    print("\nContoh peserta baru: jam belajar=6.5, kehadiran=90%, tugas=8/10")
    print("Prediksi model:", "Lulus" if hasil == 1 else "Belum Lulus")
    print("Peringatan: prediksi sintetis tidak boleh menjadi dasar keputusan pendidikan nyata.")

if __name__ == "__main__":
    main()
