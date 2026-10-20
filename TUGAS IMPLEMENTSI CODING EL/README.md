# Studi Kasus 6 Materi: Data, AI, HPC, GIS, HCI, dan Deforestasi

Repositori ini berisi enam studi kasus mini yang dapat dijalankan dengan Python. Setiap studi kasus memiliki latar belakang, tujuan, implementasi, dan cara menjalankan program.

## Daftar studi kasus

1. **Make Sense of Data with Analytics and AI** — analisis penjualan dan prediksi penjualan sederhana.
2. **Bridging Global Infrastructure to Address Local Challenges in HPC** — membandingkan waktu komputasi sekuensial dan paralel.
3. **Career and Competition in Industrial Era with GIS** — memetakan peluang kerja bidang teknologi secara sederhana berdasarkan wilayah.
4. **Introduction to Machine Learning** — klasifikasi kelulusan kursus berdasarkan data aktivitas belajar sintetis.
5. **Human-Computer Interaction & Data Visualization** — dashboard interaktif untuk memahami data penjualan.
6. **Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI** — klasifikasi indikasi perubahan tutupan lahan dari fitur satelit sintetis.

> **Catatan akademik:** dataset dalam proyek ini bersifat sintetis/demonstrasi, bukan data resmi. Hasil program tidak boleh dianggap sebagai keputusan dunia nyata. Studi kasus nomor 6 tidak menggunakan citra satelit asli dan bukan alat pemantauan hutan operasional.

## Persiapan

Disarankan menggunakan Python 3.10 atau lebih baru. Buka terminal di folder proyek, lalu jalankan:

```bash
pip install -r requirements.txt
```

Untuk menjalankan salah satu studi kasus, masuk ke foldernya. Contoh:

```bash
cd 01_data_analytics_ai
python main.py
```

Untuk dashboard pada studi kasus nomor 5:

```bash
cd 05_hci_data_visualization
streamlit run app.py
```

## Struktur folder

```text
studi_kasus_6_materi/
├── README.md
├── requirements.txt
├── 01_data_analytics_ai/
├── 02_hpc_local_challenges/
├── 03_gis_career_competition/
├── 04_machine_learning/
├── 05_hci_data_visualization/
└── 06_deforestation_ai/
```

## Ide pengembangan lanjutan

- Ganti dataset sintetis dengan data nyata yang memiliki izin penggunaan.
- Tambahkan pengujian, visualisasi, dan dokumentasi hasil.
- Untuk GIS, gunakan koordinat dan batas wilayah yang tervalidasi.
- Untuk machine learning, pisahkan data latih dan uji serta evaluasi model.
- Untuk dashboard, uji kemudahan penggunaan dengan beberapa pengguna.
- Untuk studi deforestasi, gunakan citra satelit resmi dan validasi lapangan dengan pendampingan ahli.
