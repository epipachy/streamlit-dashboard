import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============================
# 📝 Fungsi Info Gambar
# ==============================
def tampilkan_info_gambar(path, img, label):
    if img is None:
        print(f"❌ {label} tidak dapat dibaca.")
        return

    tinggi, lebar = img.shape[:2]
    mode = "Grayscale" if len(img.shape) == 2 else "RGB"
    ukuran = round(os.path.getsize(path) / 1024, 2)
    rasio_aspek = round(lebar / tinggi, 2)

    print(f"\n📌 Informasi {label}:")
    print(f"- Path file       : {path}")
    print(f"- Mode warna      : {mode}")
    print(f"- Resolusi        : {lebar} x {tinggi}")
    print(f"- Rasio aspek     : {rasio_aspek}")
    print(f"- Ukuran file     : {ukuran} KB")

# ==============================
# 📊 Fungsi Histogram
# ==============================
def tampilkan_histogram(imgA, imgB, imgC):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    data = [(imgA, "Histogram Gambar A"), 
            (imgB, "Histogram Gambar B"),
            (imgC, "Histogram Hasil Blending")]

    for i, (img, title) in enumerate(data):
        axes[i].set_title(title)
        axes[i].set_xlabel("Intensitas (0-255)")
        axes[i].set_ylabel("Jumlah Piksel")
        axes[i].hist(img.ravel(), bins=256, color='gray', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

# ==============================
# 🖼️ Fungsi Tampilkan Gambar
# ==============================
def tampilkan_gambar_layout(A, B, C):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.title("Citra A (Posisi Awal)")
    plt.imshow(A, cmap='gray')
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Citra B (Posisi Akhir)")
    plt.imshow(B, cmap='gray')
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("Hasil Blending")
    plt.imshow(C, cmap='gray')
    plt.axis("off")

    plt.tight_layout()
    plt.show()

# ==============================
# 🧮 MAIN PROGRAM
# ==============================
def main():
    print("=== 🎨 Deteksi Gerakan ===")

    # Input nama file
    pathA = input("Masukkan nama gambar A: ")
    pathB = input("Masukkan nama gambar B: ")

    # Baca citra dalam grayscale
    A = cv2.imread(pathA, cv2.IMREAD_GRAYSCALE)
    B = cv2.imread(pathB, cv2.IMREAD_GRAYSCALE)

    if A is None or B is None:
        print("❌ Salah satu gambar tidak ditemukan!")
        return

    # Samakan ukuran citra
    B = cv2.resize(B, (A.shape[1], A.shape[0]))

    # Tampilkan informasi citra
    tampilkan_info_gambar(pathA, A, "Gambar A")
    tampilkan_info_gambar(pathB, B, "Gambar B")

    # ==============================
    # 💡 Rumus Blending sesuai buku
    # ==============================
    wa = 1
    wb = -1
    C = cv2.addWeighted(A, wa, B, wb, 128)

    # ==============================
    # 💾 Simpan hasil
    # ==============================
    output_name = "hasil_deteksi_gerakan.jpg"
    cv2.imwrite(output_name, C)
    print(f"\n✅ Hasil blending disimpan sebagai: {output_name}")

    # ==============================
    # 📊 Tampilkan dan Analisis
    # ==============================
    tampilkan_gambar_layout(A, B, C)
    tampilkan_histogram(A, B, C)

    # ==============================
    # ✍️ Simpan perhitungan piksel
    # ==============================
    with open("hasil_perhitungan_gerakan.txt", "w", encoding="utf-8") as f:
        f.write("=== HASIL OPERASI BLENDING ===\n")
        f.write(f"File A : {pathA}\n")
        f.write(f"File B : {pathB}\n")
        f.write(f"Rumus  : C(x,y) = {wa}*A(x,y) + {wb}*B(x,y) + 128\n\n")

        for y in range(A.shape[0]):
            for x in range(A.shape[1]):
                c_val = int(C[y, x])
                a_val = int(A[y, x])
                b_val = int(B[y, x])
                f.write(f"C({x},{y}) = {wa}*{a_val} + {wb}*{b_val} + 128 = {c_val}\n")

    print("🧾 Semua perhitungan piksel tersimpan di: hasil_perhitungan.txt")

# ==============================
if __name__ == "__main__":
    main()
