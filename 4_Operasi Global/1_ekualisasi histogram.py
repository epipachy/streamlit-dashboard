# ==============================
# 📘 EKUALISASI HISTOGRAM + HISTOGRAM OUTPUT
# ==============================
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# === 1. INPUT GAMBAR ===
path = input("Masukkan nama/path gambar: ")

# Baca sebagai grayscale
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("\n❌ Gambar tidak ditemukan! Periksa kembali nama atau path file.")
    exit()

# === 2. INFORMASI GAMBAR ===
h, w = img.shape
k = 8
L = 2**k   # 256 level
total_pixel = w * h
ukuran_file = round(os.path.getsize(path) / 1024, 2)
rasio_aspek = round(w / h, 2)

print("\n📌 Informasi Gambar:")
print(f"- Resolusi        : {w} x {h} piksel")
print(f"- Kedalaman warna : {k} bit (grayscale)")
print(f"- Jumlah pixel    : {total_pixel}")
print(f"- Rasio aspek     : {rasio_aspek} (lebar/tinggi)")
print(f"- Ukuran file     : {ukuran_file} KB")

# === 3. HITUNG HISTOGRAM ===
hist, _ = np.histogram(img.flatten(), bins=L, range=[0, L])

# === 4. HITUNG CDF (Ci) ===
cdf = hist.cumsum()

# === 5. RUMUS BUKU: Ko = round( Ci * (2^k - 1) / (w * h) ) ===
Ko = np.round((cdf * (L - 1)) / total_pixel).astype(np.uint8)

# === 6. BUAT GAMBAR HASIL EKUALISASI ===
img_equalized = Ko[img]

# === 7. SIMPAN KE FILE TXT ===
output_txt = "hasil_perhitungan_ekualisasi.txt"
with open(output_txt, "w", encoding="utf-8") as f:
    f.write("=== HASIL PERHITUNGAN EKUALISASI HISTOGRAM ===\n")
    f.write(f"File gambar: {path}\n")
    f.write(f"Resolusi   : {w} x {h}\n")
    f.write(f"Jumlah pixel: {total_pixel}\n")
    f.write(f"Skala keabuan (k): {k} bit\n")
    f.write(f"L = {L}\n\n")
    f.write(f"{'Nilai Keabuan':<15}{'Frekuensi (fi)':<20}{'Ci (CDF)':<20}{'Nilai Baru (Ko)':<20}\n")
    f.write("="*75 + "\n")

    for i in range(L):
        if hist[i] > 0:
            f.write(f"{i:<15}{hist[i]:<20}{cdf[i]:<20}{Ko[i]:<20}\n")

print(f"\n📄 Data ekualisasi berhasil disimpan ke: {output_txt}")

# === 8. TAMPILKAN CITRA DAN HISTOGRAM ===
plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(img_equalized, cmap='gray')
plt.title("Citra Setelah Ekualisasi")
plt.axis("off")

plt.subplot(2,2,3)
plt.hist(img.flatten(), bins=256, range=[0,256], color='gray')
plt.title("Histogram Asli")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Frekuensi")

plt.subplot(2,2,4)
plt.hist(img_equalized.flatten(), bins=256, range=[0,256], color='gray')
plt.title("Histogram Setelah Ekualisasi")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Frekuensi")

plt.tight_layout()
plt.show()

# === 9. SIMPAN GAMBAR ===
cv2.imwrite("hasil_ekualisasi.jpg", img_equalized)
print("💾 Hasil citra disimpan sebagai: hasil_ekualisasi.jpg")
