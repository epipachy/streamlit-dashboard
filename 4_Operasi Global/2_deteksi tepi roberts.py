# ==============================
# 📘 ROBERTS EDGE DETECTION (MANUAL) + HISTOGRAM
# ==============================
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# === 1. INPUT GAMBAR ===
path = input("Masukkan nama / path gambar: ")

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("\n❌ Gambar tidak ditemukan! Periksa kembali path atau nama file.")
    exit()

# === 2. INFORMASI GAMBAR ===
h, w = img.shape
ukuran_file = round(os.path.getsize(path) / 1024, 2)
rasio_aspek = round(w / h, 2)

print("\n📌 Informasi Gambar:")
print(f"- Resolusi        : {w} x {h} piksel")
print(f"- Kedalaman warna : 8 bit (grayscale)")
print(f"- Rasio aspek     : {rasio_aspek} (lebar/tinggi)")
print(f"- Ukuran file     : {ukuran_file} KB")

# === 3. DEFINISI KERNEL ROBERTS ===
K1 = np.array([[1, 0],
               [0, -1]])

K2 = np.array([[0, 1],
               [-1, 0]])

# === 4. PROSES CONVOLUTION MANUAL ===
output = np.zeros((h, w), dtype=np.float32)

for i in range(h - 1):
    for j in range(w - 1):
        region = img[i:i+2, j:j+2]

        Gx = np.sum(region * K1)
        Gy = np.sum(region * K2)

        magnitude = np.sqrt(Gx**2 + Gy**2)
        output[i, j] = magnitude

# === 5. NORMALISASI HASIL KE 0–255 ===
output = np.clip(output, 0, 255).astype(np.uint8)

# === 6. SIMPAN PERHITUNGAN KE FILE TXT ===
output_txt = "hasil_roberts_operator.txt"

with open(output_txt, "w") as f:
    f.write("=== HASIL PERHITUNGAN ROBERTS OPERATOR ===\n\n")
    f.write(f"File Input     : {path}\n")
    f.write(f"Resolusi       : {w} x {h}\n\n")
    f.write("[i,j] -> Gx, Gy, Magnitude\n\n")

    for i in range(h - 1):
        for j in range(w - 1):
            region = img[i:i+2, j:j+2]
            Gx = np.sum(region * K1)
            Gy = np.sum(region * K2)
            magnitude = np.sqrt(Gx**2 + Gy**2)
            f.write(f"[{i},{j}] -> Gx={Gx}, Gy={Gy}, M={round(magnitude,2)}\n")

print(f"\n📄 Hasil perhitungan disimpan ke: {output_txt}")

# === 7. TAMPILKAN GAMBAR & HISTOGRAM ===
plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Citra Asli")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(output, cmap='gray')
plt.title("Hasil Deteksi Tepi (Roberts)")
plt.axis('off')

# Histogram asli
plt.subplot(2,2,3)
plt.hist(img.flatten(), bins=256, range=[0,256], color='gray')
plt.xlabel("Intensitas Piksel")
plt.ylabel("Frekuensi")
plt.title("Histogram Citra Asli")

# Histogram hasil
plt.subplot(2,2,4)
plt.hist(output.flatten(), bins=256, range=[0,256], color='gray')
plt.xlabel("Intensitas Piksel")
plt.ylabel("Frekuensi")
plt.title("Histogram Setelah Roberts Detection")

plt.tight_layout()
plt.show()

# === 8. SIMPAN HASIL GAMBAR ===
cv2.imwrite("hasil_roberts.jpg", output)
print("💾 Hasil citra tepi disimpan sebagai: hasil_roberts.jpg")
