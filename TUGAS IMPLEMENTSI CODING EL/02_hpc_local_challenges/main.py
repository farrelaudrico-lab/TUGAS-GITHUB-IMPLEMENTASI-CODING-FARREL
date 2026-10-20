import time
import os
from concurrent.futures import ProcessPoolExecutor

def hitung_jumlah_kuadrat(rentang):
    mulai, akhir = rentang
    return sum(i * i for i in range(mulai, akhir))

def main():
    jumlah_data = 1_000_000
    jumlah_bagian = max(2, os.cpu_count() or 2)
    ukuran_bagian = jumlah_data // jumlah_bagian
    bagian = []
    awal = 0
    while awal < jumlah_data:
        akhir = min(awal + ukuran_bagian, jumlah_data)
        bagian.append((awal, akhir))
        awal = akhir

    t0 = time.perf_counter()
    hasil_sekuensial = hitung_jumlah_kuadrat((0, jumlah_data))
    waktu_sekuensial = time.perf_counter() - t0

    t1 = time.perf_counter()
    # Batasi worker agar tidak membuat terlalu banyak proses pada komputer kecil.
    with ProcessPoolExecutor(max_workers=min(jumlah_bagian, 4)) as executor:
        hasil_bagian = list(executor.map(hitung_jumlah_kuadrat, bagian))
    hasil_paralel = sum(hasil_bagian)
    waktu_paralel = time.perf_counter() - t1

    print("=== PERBANDINGAN HPC SEDERHANA ===")
    print(f"Jumlah data       : {jumlah_data:,}")
    print(f"Jumlah CPU logis  : {os.cpu_count()}")
    print(f"Hasil sekuensial  : {hasil_sekuensial:,}")
    print(f"Hasil paralel     : {hasil_paralel:,}")
    print(f"Waktu sekuensial  : {waktu_sekuensial:.4f} detik")
    print(f"Waktu paralel     : {waktu_paralel:.4f} detik")
    print("Hasil sama        :", hasil_sekuensial == hasil_paralel)
    print("\nInterpretasi: waktu paralel dapat lebih cepat atau lebih lambat karena overhead proses.")

if __name__ == "__main__":
    main()
