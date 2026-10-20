import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Penjualan", page_icon="📊", layout="wide")
st.title("Dashboard Analisis Penjualan")
st.caption("Studi kasus HCI dan visualisasi data — dataset sintetis untuk pembelajaran.")

df = pd.DataFrame({
    "Tanggal": pd.to_datetime([
        "2026-01-03","2026-01-05","2026-01-08","2026-01-12","2026-01-15",
        "2026-02-02","2026-02-06","2026-02-10","2026-02-14","2026-02-20",
        "2026-03-01","2026-03-04","2026-03-09","2026-03-15","2026-03-22"
    ]),
    "Kategori": ["Elektronik","Aksesori","Elektronik","Alat Tulis","Aksesori",
                 "Elektronik","Alat Tulis","Aksesori","Elektronik","Alat Tulis",
                 "Aksesori","Elektronik","Alat Tulis","Aksesori","Elektronik"],
    "Produk": ["Headset","Mousepad","Keyboard","Buku","Mouse",
               "Mouse","Pulpen","Keyboard","Headset","Buku",
               "Mousepad","Keyboard","Pulpen","Mouse","Headset"],
    "Jumlah": [2,5,3,10,4,6,20,2,3,8,7,4,15,5,2],
    "Harga": [350000,50000,300000,25000,150000,150000,5000,300000,350000,25000,
              50000,300000,5000,150000,350000]
})
df["Pendapatan"] = df["Jumlah"] * df["Harga"]

kategori = st.selectbox("Pilih kategori produk", ["Semua"] + sorted(df["Kategori"].unique().tolist()))
filtered = df if kategori == "Semua" else df[df["Kategori"] == kategori]

total = int(filtered["Pendapatan"].sum())
transaksi = len(filtered)
unit = int(filtered["Jumlah"].sum())
c1, c2, c3 = st.columns(3)
c1.metric("Total pendapatan", f"Rp{total:,.0f}".replace(",", "."))
c2.metric("Jumlah transaksi", transaksi)
c3.metric("Unit terjual", unit)

left, right = st.columns(2)
with left:
    by_date = filtered.groupby("Tanggal", as_index=False)["Pendapatan"].sum()
    fig = px.line(by_date, x="Tanggal", y="Pendapatan", markers=True,
                  title="Pendapatan berdasarkan tanggal")
    st.plotly_chart(fig, use_container_width=True)
with right:
    by_product = filtered.groupby("Produk", as_index=False)["Jumlah"].sum()
    fig2 = px.bar(by_product, x="Produk", y="Jumlah", title="Unit terjual per produk")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Data transaksi")
st.dataframe(filtered, use_container_width=True, hide_index=True)
st.info("Catatan: angka merupakan data contoh. Untuk penggunaan nyata, lakukan pengujian kegunaan dan validasi data.")
