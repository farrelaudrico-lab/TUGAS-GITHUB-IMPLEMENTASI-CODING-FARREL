import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    # Dataset sintetis: jumlah unit terjual per produk dan bulan
    data = pd.DataFrame({
        "bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"] * 3,
        "nomor_bulan": list(range(1, 7)) * 3,
        "produk": ["Laptop"] * 6 + ["Mouse"] * 6 + ["Keyboard"] * 6,
        "harga": [7_000_000] * 6 + [150_000] * 6 + [300_000] * 6,
        "unit_terjual": [8, 9, 11, 10, 13, 15, 25, 28, 31, 30, 35, 39,
                         12, 14, 15, 18, 17, 21]
    })
    data["pendapatan"] = data["harga"] * data["unit_terjual"]

    print("=== RINGKASAN DATA ===")
    print(data.head(8).to_string(index=False))

    print("\n=== PENDAPATAN PER PRODUK ===")
    print(data.groupby("produk")["pendapatan"].sum().sort_values(ascending=False).to_string())

    print("\n=== PENDAPATAN PER BULAN ===")
    print(data.groupby(["nomor_bulan", "bulan"])["pendapatan"].sum().to_string())

    # Contoh prediksi untuk Laptop berdasarkan tren unit terjual.
    laptop = data[data["produk"] == "Laptop"]
    model = LinearRegression()
    model.fit(laptop[["nomor_bulan"]], laptop["unit_terjual"])
    prediksi_juli = model.predict(pd.DataFrame({"nomor_bulan": [7]}))[0]
    print(f"\nPrediksi unit Laptop pada Juli (model linear sederhana): {prediksi_juli:.1f} unit")
    print("Catatan: prediksi hanya demonstrasi berdasarkan enam titik data sintetis.")

if __name__ == "__main__":
    main()
