
from faker import Faker
import pandas as pd
import random
import os
from datetime import date, datetime, timedelta

fake = Faker("id_ID")

Faker.seed(42)
random.seed(42)

today = date.today()

# ==========================================
# 1. MEMBACA DATA MEMBER
# ==========================================

member_df = pd.read_csv("data_member_clean_awal.csv")

# Pisahkan data member berdasarkan ID
member_data = member_df[
    ["ID", "Nama", "Pilihan Paket"]
].to_dict("records")

# ==========================================
# 2. DATA REFERENSI
# ==========================================

metode_pembayaran = ["Cash", "Transfer", "QRIS"]

produk_list = [
    "Air Mineral",
    "Minuman Isotonik",
    "Protein Shake",
    "Kopi",
    "Tidak Ada"
]

loker_list = [f"L{i:02}" for i in range(1, 51)]

nama_non_member = [
    fake.first_name() + " " + fake.last_name()
    for _ in range(100)
]

# ==========================================
# 3. MEMBUAT 200 DATA KUNJUNGAN NORMAL
# ==========================================

data = []

for i in range(200):

    # Pembagian 150 member dan 50 non-member
    if i < 150:
        status_pengunjung = "Member"

        # Mengambil member secara acak.
        # Member yang sama boleh muncul berkali-kali.
        member = random.choice(member_data)

        id_member = member["ID"]
        nama = member["Nama"]
        paket = member["Pilihan Paket"]

    else:
        status_pengunjung = "Non-member"

        id_member = None
        nama = random.choice(nama_non_member)
        paket = "Harian"

    # Tanggal kunjungan dalam 90 hari terakhir
    tanggal = today - timedelta(days=random.randint(0, 90))

    # Waktu masuk antara pukul 06.00 sampai 20.00
    jam_masuk = random.randint(6, 20)
    menit_masuk = random.choice([0, 15, 30, 45])

    waktu_masuk = datetime.strptime(
        f"{jam_masuk:02}:{menit_masuk:02}",
        "%H:%M"
    )

    # Durasi latihan antara 45 menit sampai 3 jam
    durasi = random.randint(45, 180)

    waktu_keluar = waktu_masuk + timedelta(minutes=durasi)

    # Produk tambahan
    produk = random.choice(produk_list)

    # Metode pembayaran:
    # Member tidak selalu melakukan transaksi saat berkunjung.
    if status_pengunjung == "Non-member" or produk != "Tidak Ada":
        metode = random.choice(metode_pembayaran)
    else:
        metode = None

    data.append({
        "ID Kunjungan": f"K{i+1:03}",
        "Tanggal": tanggal,
        "ID Member": id_member,
        "Nama Pengunjung": nama,
        "Status Pengunjung": status_pengunjung,
        "Paket/Layanan": paket,
        "Nomor Loker": random.choice(loker_list),
        "Waktu Masuk": waktu_masuk.strftime("%H:%M"),
        "Waktu Keluar": waktu_keluar.strftime("%H:%M"),
        "Metode Pembayaran": metode,
        "Produk Tambahan": produk
    })

df = pd.DataFrame(data)

# Simpan dataset awal yang relatif bersih
df.to_csv("data_kunjungan_clean_awal.csv", index=False)

# ==========================================
# 4. MEMBUAT DATA KOTOR (RAW DATA)
# ==========================================

df_raw = df.copy()

# 4.1 Status pengunjung tidak konsisten
idx = random.sample(list(df_raw.index), 20)

for i in idx:
    if df_raw.loc[i, "Status Pengunjung"] == "Member":
        df_raw.loc[i, "Status Pengunjung"] = random.choice(
            ["member", "MEMBER", "Mbr"]
        )
    else:
        df_raw.loc[i, "Status Pengunjung"] = random.choice(
            ["non member", "NON-MEMBER", "Non member"]
        )

# 4.2 Metode pembayaran tidak konsisten
idx = random.sample(list(df_raw.index), 15)

variasi_metode = {
    "Cash": ["cash", "Tunai", "CASH"],
    "Transfer": ["transfer", "TF", "TRANSFER"],
    "QRIS": ["qris", "Qris", "QRIS "]
}

for i in idx:
    metode = df_raw.loc[i, "Metode Pembayaran"]

    if pd.notna(metode):
        df_raw.loc[i, "Metode Pembayaran"] = random.choice(
            variasi_metode[metode]
        )

# 4.3 Nomor loker kosong
idx = random.sample(list(df_raw.index), 20)
df_raw.loc[idx, "Nomor Loker"] = None

# 4.4 Format nama tidak konsisten
idx = random.sample(list(df_raw.index), 15)

for i in idx:
    df_raw.loc[i, "Nama Pengunjung"] = (
        " " + df_raw.loc[i, "Nama Pengunjung"].lower() + " "
    )

# 4.5 Waktu masuk tidak valid
idx = random.sample(list(df_raw.index), 8)

for i in idx:
    df_raw.loc[i, "Waktu Masuk"] = random.choice(
        ["25:90", "99:99", "abc", "24:75"]
    )

# 4.6 Waktu keluar lebih awal daripada waktu masuk
idx = random.sample(list(df_raw.index), 8)

for i in idx:
    df_raw.loc[i, "Waktu Keluar"] = "05:00"

# 4.7 Format paket tidak konsisten
idx = random.sample(list(df_raw.index), 15)

for i in idx:
    paket = df_raw.loc[i, "Paket/Layanan"]

    variasi_paket = {
        "Gym": ["gym", "GYM", " Gym "],
        "Gym + Treadmill": [
            "gym+treadmill",
            "Gym + treadmill",
            "GYM + TREADMILL"
        ],
        "Harian": ["harian", "HARIAN", " Harian "]
    }

    df_raw.loc[i, "Paket/Layanan"] = random.choice(
        variasi_paket[paket]
    )

# 4.8 Produk tambahan tidak konsisten
idx = random.sample(list(df_raw.index), 15)

for i in idx:
    produk = df_raw.loc[i, "Produk Tambahan"]

    if produk == "Tidak Ada":
        df_raw.loc[i, "Produk Tambahan"] = random.choice(
            ["-", "tidak ada", "", None]
        )
    else:
        df_raw.loc[i, "Produk Tambahan"] = (
            df_raw.loc[i, "Produk Tambahan"].upper()
        )

# 4.9 Tanggal kosong
idx = random.sample(list(df_raw.index), 5)
df_raw.loc[idx, "Tanggal"] = None

# 4.10 ID Member tidak ditemukan
idx = random.sample(
    list(df_raw[df_raw["Status Pengunjung"] == "Member"].index),
    5
)

for i in idx:
    df_raw.loc[i, "ID Member"] = "M999"

# 4.11 Duplikasi data kunjungan
df_raw = pd.concat(
    [df_raw, df_raw.sample(5, random_state=42)],
    ignore_index=True
)

# ==========================================
# 5. SIMPAN RAW DATASET
# ==========================================

df_raw.to_csv("data_kunjungan_raw.csv", index=False)

print("=== DATA KUNJUNGAN RAW ===")
print(df_raw.head(15))

print("\nTotal data normal:", len(df))
print("Total data raw:", len(df_raw))

print("\nJumlah missing value:")
print(df_raw.isnull().sum())

print("\nJumlah duplikasi:")
print(df_raw.duplicated().sum())

print("\nDistribusi status pengunjung:")
print(df_raw["Status Pengunjung"].value_counts())

print("\nLokasi file:")
print(os.path.abspath("data_kunjungan_raw.csv"))
