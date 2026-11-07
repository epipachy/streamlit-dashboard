# =============================================
# 📘 SMOOTHING CITRA (5 titik, 3x3, 5x5) – RGB
# =============================================
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# === 1. INPUT GAMBAR ===
path = input("Masukkan nama / path gambar: ")

img = cv2.imread(path)
if img is None:
    print("\n❌ Gambar tidak ditemukan!")
    exit()

# Ubah BGR → RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w, c = img.shape
ukuran_file = round(os.path.getsize(path) / 1024, 2)
rasio_aspek = round(w / h, 2)

print("\n📌 Informasi Gambar:")
print(f"- Resolusi        : {w} x {h} piksel")
print(f"- Mode            : RGB (berwarna)")
print(f"- Rasio aspek     : {rasio_aspek}")
print(f"- Ukuran file     : {ukuran_file} KB")


# === 2. DEFINISI KERNEL SMOOTHING ===

# 5 titik bertetangga (Cross Kernel)
K5 = np.array([
    [0,   1/5, 0],
    [1/5, 1/5, 1/5],
    [0,   1/5, 0]
])

# 3x3 (9 titik)
K3 = np.ones((3,3), dtype=np.float32) / 9

# 5x5 (25 titik)
K25 = np.ones((5,5), dtype=np.float32) / 25


# === 3. FUNGSI CONVOLUTION UNTUK RGB ===
def convolution_rgb(image, kernel):
    h, w, c = image.shape
    kh, kw = kernel.shape
    pad = kh // 2

    # hasil output
    output = np.zeros_like(image, dtype=np.float32)

    # padding
    padded = np.pad(image, ((pad,pad),(pad,pad),(0,0)), mode='constant')

    # proses per piksel
    for y in range(h):
        for x in range(w):
            region = padded[y:y+kh, x:x+kw, :]

            # proses per channel (R,G,B)
            for ch in range(3):
                output[y, x, ch] = np.sum(region[:,:,ch] * kernel)

    return np.clip(output, 0, 255).astype(np.uint8)


# === 4. PROSES SMOOTHING ===
img_smooth_5 = convolution_rgb(img, K5)
img_smooth_3 = convolution_rgb(img, K3)
img_smooth_25 = convolution_rgb(img, K25)

# === 5. TAMPILKAN HASIL ===
plt.figure(figsize=(12, 8))

plt.subplot(2,2,1)
plt.imshow(img)
plt.title("Citra Asli (RGB)")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(img_smooth_5)
plt.title("Smoothing 5 Titik")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(img_smooth_3)
plt.title("Smoothing 3×3 (9 titik)")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(img_smooth_25)
plt.title("Smoothing 5×5 (25 titik)")
plt.axis("off")

plt.tight_layout()
plt.show()

# === 6. SIMPAN ===
cv2.imwrite("smooth_5_titik.jpg", cv2.cvtColor(img_smooth_5, cv2.COLOR_RGB2BGR))
cv2.imwrite("smooth_3x3.jpg", cv2.cvtColor(img_smooth_3, cv2.COLOR_RGB2BGR))
cv2.imwrite("smooth_5x5.jpg", cv2.cvtColor(img_smooth_25, cv2.COLOR_RGB2BGR))

print("\n💾 File disimpan sebagai:")
print("- smooth_5_titik.jpg")
print("- smooth_3x3.jpg")
print("- smooth_5x5.jpg")
