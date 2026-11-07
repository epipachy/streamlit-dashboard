import cv2
import numpy as np

# ==========================
# 1. INPUT GAMBAR
# ==========================
path = input("Masukkan path gambar: ")
img = cv2.imread(path)

if img is None:
    print("Gambar tidak ditemukan! Periksa path.")
    exit()

# Tampilkan ukuran gambar
h, w = img.shape[:2]
print(f"Ukuran gambar: {w} x {h}")

# ==========================
# 2. FLIPPING
# ==========================
print("\nPilih jenis flipping:")
print("1 = Horizontal (mirror kiri-kanan)")
print("2 = Vertical (atas-bawah)")
print("3 = Kombinasi (horizontal + vertical)")
print("0 = Tidak melakukan flipping")

flip_choice = int(input("Masukkan pilihan (0/1/2/3): "))

if flip_choice == 1:
    img = cv2.flip(img, 1)   # flip horizontal
elif flip_choice == 2:
    img = cv2.flip(img, 0)   # flip vertical
elif flip_choice == 3:
    img = cv2.flip(img, -1)  # flip keduanya
else:
    print("Tidak melakukan flipping.")

# ==========================
# 3. ROTASI
# ==========================
angle = float(input("\nMasukkan derajat rotasi (misal 45, 90, -30): "))

# Membuat matriks rotasi
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)

# Melakukan rotasi
rotated = cv2.warpAffine(img, M, (w, h))

# ==========================
# 4. TAMPILKAN & SIMPAN
# ==========================
cv2.imshow("Hasil", rotated)
cv2.imwrite("hasil_flipped_rotated.png", rotated)
print("\nHasil disimpan sebagai: hasil_flipped_rotated.png")
cv2.waitKey(0)
cv2.destroyAllWindows()
