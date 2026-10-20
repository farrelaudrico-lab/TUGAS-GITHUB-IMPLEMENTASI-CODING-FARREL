import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Koordinat dan angka merupakan data ilustrasi, bukan statistik resmi.
    df = pd.DataFrame({
        "kota": ["Bengkulu", "Jakarta", "Bandung", "Yogyakarta", "Surabaya"],
        "longitude": [102.2655, 106.8456, 107.6191, 110.3695, 112.7521],
        "latitude": [-3.8004, -6.2088, -6.9175, -7.7956, -7.2575],
        "lowongan_teknologi": [35, 220, 130, 90, 115],
        "kandidat": [120, 900, 500, 420, 460]
    })
    df["rasio_lowongan_per_kandidat"] = df["lowongan_teknologi"] / df["kandidat"]
    df["indikasi_persaingan"] = 1 / df["rasio_lowongan_per_kandidat"]

    print("=== DATA PELUANG KERJA (SINTETIS) ===")
    print(df[["kota", "lowongan_teknologi", "kandidat",
              "rasio_lowongan_per_kandidat"]].to_string(index=False,
              formatters={"rasio_lowongan_per_kandidat": "{:.3f}".format}))
    print("\nRasio lebih tinggi berarti lebih banyak lowongan relatif terhadap kandidat dalam data contoh.")
    print("\nPeringkat rasio:")
    print(df.sort_values("rasio_lowongan_per_kandidat", ascending=False)
            [["kota", "rasio_lowongan_per_kandidat"]].to_string(index=False))

    plt.figure(figsize=(9, 5))
    plt.scatter(df["longitude"], df["latitude"], s=df["lowongan_teknologi"] * 2, alpha=0.65)
    for _, row in df.iterrows():
        plt.annotate(row["kota"], (row["longitude"], row["latitude"]), xytext=(5, 5),
                     textcoords="offset points")
    plt.title("Ilustrasi Sebaran Peluang Kerja Teknologi")
    plt.xlabel("Longitude (bukan peta batas wilayah)")
    plt.ylabel("Latitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("peta_peluang_kerja.png", dpi=150)
    print("\nGrafik disimpan sebagai peta_peluang_kerja.png")

if __name__ == "__main__":
    main()
