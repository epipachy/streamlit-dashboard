
import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Summit Gym Dashboard",
    page_icon="💪",
    layout="wide"
)

# Judul
st.title("💪 Summit Gym Dashboard")
st.write("Dashboard Pengelolaan Member dan Kunjungan")

st.divider()

# Data dummy
data_member = {
    "ID Member": ["M001", "M002", "M003", "M004", "M005"],
    "Nama": ["Andi", "Budi", "Citra", "Dinda", "Eko"],
    "Paket": ["Bulanan", "Harian", "Bulanan", "Tahunan", "Bulanan"],
    "Status": ["Aktif", "Aktif", "Expired", "Aktif", "Hampir Habis"]
}

df = pd.DataFrame(data_member)

# Metrik
col1, col2, col3 = st.columns(3)

col1.metric("Total Member", len(df))
col2.metric("Member Aktif", 3)
col3.metric("Total Kunjungan", 125)

st.divider()

# Grafik kunjungan
st.subheader("Grafik Kunjungan Mingguan")

kunjungan = pd.DataFrame({
    "Hari": ["Senin", "Selasa", "Rabu", "Kamis",
             "Jumat", "Sabtu", "Minggu"],
    "Jumlah Kunjungan": [15, 20, 18, 25, 30, 35, 22]
})

st.bar_chart(
    kunjungan,
    x="Hari",
    y="Jumlah Kunjungan"
)

# Tabel member
st.subheader("Data Member")
st.dataframe(df, use_container_width=True)

# Sidebar
st.sidebar.title("Navigasi")
st.sidebar.write("Dashboard Summit Gym")
