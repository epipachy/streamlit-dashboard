
from faker import Faker
import pandas as pd
import random
from datetime import date, timedelta

fake = Faker("id_ID")

Faker.seed(42)
random.seed(42)

# Tanggal acuan
today = date.today()

# Nama yang lebih sederhana
nama_depan = [
    "Andi", "Budi", "Dimas", "Rizky", "Fajar",
    "Agus", "Rian", "Bagas", "Aditya", "Arif",
    "Siti", "Putri", "Dewi", "Ayu", "Nadia",
    "Rani", "Intan", "Dinda", "Nisa", "Citra"
]

nama_belakang = [
    "Pratama", "Saputra", "Wijaya", "Santoso",
    "Ramadhan", "Permana", "Kurniawan", "Setiawan",
    "Lestari", "Anggraini", "Puspita", "Wulandari",
    "Maulana", "Hidayat", "Nugroho", "Firmansyah"
]

# Wilayah di Kota Semarang
wilayah_semarang = [
    ("Tembalang", "Bulusan"),
    ("Tembalang", "Meteseh"),
    ("Tembalang", "Sendangmulyo"),
    ("Tembalang", "Kramas"),
    ("Banyumanik", "Pedalangan"),
    ("Banyumanik", "Srondol Wetan"),
    ("Banyumanik", "Ngesrep"),
    ("Pedurungan", "Tlogosari Kulon"),
    ("Pedurungan", "Gemah"),
    ("Pedurungan", "Pedurungan Tengah"),
    ("Candisari", "Jatingaleh"),
    ("Candisari", "Tegalsari"),
    ("Semarang Barat", "Manyaran"),
    ("Semarang Barat", "Kembangarum"),
    ("Semarang Selatan", "Pleburan")
]

# Sesuaikan dengan paket asli Summit Gym.
# Angka menunjukkan durasi membership dalam hari.
paket_durasi = {
    "Gym": 30,
    "Gym + Treadmill": 30
}

# Atur jumlah masing-masing status
status_list = (
    ["Aktif"] * 60 +
    ["Segera Berakhir"] * 25 +
    ["Kadaluwarsa"] * 15
)

random.shuffle(status_list)

data = []

for i in range(100):

    # Gender dan nama
    gender = random.choice(["Laki-laki", "Perempuan"])

    nama = (
        random.choice(nama_depan) + " " +
        random.choice(nama_belakang)
    )

    # Alamat Semarang
    kecamatan, kelurahan = random.choice(wilayah_semarang)

    alamat = (
        f"Jl. {fake.last_name()} No. {random.randint(1, 150)}, "
        f"Kel. {kelurahan}, Kec. {kecamatan}, "
        f"Kota Semarang, Jawa Tengah"
    )

    # Paket membership
    paket = random.choice(list(paket_durasi.keys()))
    durasi = paket_durasi[paket]

    # Status ditentukan berdasarkan distribusi yang sudah dibuat
    status = status_list[i]

    if status == "Kadaluwarsa":
        tgl_akhir = today - timedelta(days=random.randint(1, 180))

    elif status == "Segera Berakhir":
        tgl_akhir = today + timedelta(days=random.randint(1, 7))

    else:
        tgl_akhir = today + timedelta(
            days=random.randint(8, durasi - 1)
        )

    # Tanggal mulai dihitung berdasarkan durasi paket
    tgl_mulai = tgl_akhir - timedelta(days=durasi)

    # Nomor telepon Indonesia
    nomor_telepon = f"08{random.randint(1000000000, 9999999999)}"

    data.append({
        "ID": f"M{i+1:03}",
        "Nama": nama,
        "Alamat": alamat,
        "Pilihan Paket": paket,
        "Tgl Mulai": tgl_mulai,
        "Tgl Akhir": tgl_akhir,
        "Nomor Telepon": nomor_telepon,
        "Status aktif": status,
        "Gender": gender
    })

df = pd.DataFrame(data)


# ==========================================
# MEMBUAT RAW DATASET (DATA KOTOR)
# ==========================================

# Salin dataset normal
df_raw = df.copy()

# 1. Nama dengan format tidak konsisten
idx = random.sample(list(df_raw.index), 5)

for i in idx:
    df_raw.loc[i, "Nama"] = (
        " " + df_raw.loc[i, "Nama"].lower() + " "
    )

# 2. Format gender tidak konsisten
idx = random.sample(list(df_raw.index), 5)

for i in idx:
    if df_raw.loc[i, "Gender"] == "Laki-laki":
        df_raw.loc[i, "Gender"] = "L"
    else:
        df_raw.loc[i, "Gender"] = "P"

# 3. Nomor telepon kosong
idx = random.sample(list(df_raw.index), 5)

df_raw.loc[idx, "Nomor Telepon"] = None

# 4. Nomor telepon tidak valid
idx = random.sample(list(df_raw.index), 3)

for i in idx:
    df_raw.loc[i, "Nomor Telepon"] = "12345"

# 5. Alamat dengan format tidak konsisten
idx = random.sample(list(df_raw.index), 5)

for i in idx:
    df_raw.loc[i, "Alamat"] = (
        df_raw.loc[i, "Alamat"].replace(
            "Kota Semarang", "semarang"
        )
    )

# 6. Duplikasi satu data member
df_raw = pd.concat(
    [df_raw, df_raw.iloc[[0]]],
    ignore_index=True
)

# ==========================================
# SIMPAN DATASET
# ==========================================

# Dataset normal
df.to_csv("data_member_clean_awal.csv", index=False)

# Dataset yang sudah diberi anomali
df_raw.to_csv("data_member_raw.csv", index=False)

print("\n=== RAW DATASET ===")
print(df_raw.head(10))

print("\nTotal data raw:", len(df_raw))

print("\nJumlah missing value:")
print(df_raw.isnull().sum())

print("\nJumlah duplikasi:")
print(df_raw.duplicated().sum())

print("\nFile tersimpan:")
import os
print(os.path.abspath("data_member_raw.csv"))

