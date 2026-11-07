from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    # 1️⃣ Input gambar
    image_path = input("Masukkan nama gambar: ")
    try:
        img_open = Image.open(image_path)

        if img_open.mode == "L":
            # Sudah grayscale, langsung dipakai
            img = img_open
            print("➡️ Gambar sudah grayscale, langsung digunakan.")
        else:
            # Kalau masih warna, konversi dengan rata-rata (R+G+B)/3
            img_rgb = img_open.convert("RGB")
            img_array_rgb = np.array(img_rgb, dtype=np.uint8)
            gray_avg = ((img_array_rgb[:,:,0].astype(int) + 
                         img_array_rgb[:,:,1].astype(int) + 
                         img_array_rgb[:,:,2].astype(int)) // 3).astype(np.uint8)
            img = Image.fromarray(gray_avg)
            print("➡️ Gambar warna dikonversi ke grayscale (average).")

    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    # ✅ Ambil informasi gambar
    format_file = img.format if img.format else os.path.splitext(image_path)[1].upper()
    mode_warna = "Grayscale (Average)" if img_open.mode != "L" else "Grayscale (Asli)"
    resolusi = img.size
    kedalaman = 8  # grayscale = 8 bit
    rasio_aspek = round(resolusi[0] / resolusi[1], 2)
    ukuran_file = round(os.path.getsize(image_path) / 1024, 2)  # KB

    print("\n📌 Informasi Gambar:")
    print(f"- Format file     : {format_file}")
    print(f"- Mode warna      : {mode_warna}")
    print(f"- Resolusi        : {resolusi} piksel")
    print(f"- Kedalaman warna : {kedalaman} bit (per piksel)")
    print(f"- Rasio aspek     : {rasio_aspek} (lebar/tinggi)")
    print(f"- Ukuran file     : {ukuran_file} KB")

    # 2️⃣ Pilih jenis thresholding
    jenis = input("\nPilih thresholding (tunggal/ganda): ").strip().lower()
    img_array = np.array(img, dtype=np.uint8)

    if jenis == "tunggal":
        ambang = int(input("Masukkan nilai ambang: "))

        # Rumus:
        # Ko = 0 jika Ki < ambang, else 1
        Ko = np.where(img_array < ambang, 0, 1).astype(np.uint8) * 255

        txt_name = "hasil_threshold_tunggal.txt"
        with open(txt_name, "w") as f:
            h, w = img_array.shape
            f.write(f"Gambar: {image_path}\nUkuran: {h} x {w}\nAmbang: {ambang}\n\n")
            for y in range(h):
                for x in range(w):
                    f.write(f"f({x},{y}) = {img_array[y,x]} -> {Ko[y,x]}\n")

    elif jenis == "ganda":
        ambang_bawah = int(input("Masukkan ambang bawah: "))
        ambang_atas = int(input("Masukkan ambang atas: "))

        # Rumus:
        # Ko = 1 jika ambang_bawah ≤ Ki ≤ ambang_atas, else 0
        Ko = np.where((img_array >= ambang_bawah) & (img_array <= ambang_atas), 1, 0).astype(np.uint8) * 255

        txt_name = "hasil_threshold_ganda.txt"
        with open(txt_name, "w") as f:
            h, w = img_array.shape
            f.write(f"Gambar: {image_path}\nUkuran: {h} x {w}\nAmbang bawah: {ambang_bawah}, Ambang atas: {ambang_atas}\n\n")
            for y in range(h):
                for x in range(w):
                    f.write(f"f({x},{y}) = {img_array[y,x]} -> {Ko[y,x]}\n")
    else:
        print("Pilihan salah. Ketik 'tunggal' atau 'ganda'.")
        return

    print(f"\n✅ Semua nilai f(x,y) sudah disimpan di file: {txt_name}")

    # 3️⃣ Konversi hasil kembali ke gambar
    img_thresh = Image.fromarray(Ko)

    # 4️⃣ Tampilkan gambar asli & hasil threshold
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Gambar Asli (Grayscale)")
    plt.imshow(img, cmap="gray")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.title(f"Hasil Thresholding ({jenis})")
    plt.imshow(img_thresh, cmap="gray")
    plt.axis("off")

    plt.show()

    # 5️⃣ Histogram sebelum & sesudah
    plt.figure(figsize=(12,5))

    # Histogram asli (grayscale normal 0-255)
    plt.subplot(1,2,1)
    plt.title("Histogram Asli (Grayscale)")
    plt.hist(img_array.flatten(), bins=256, range=(0,256), color="gray", alpha=0.7)
    plt.xlabel("Intensitas Piksel (0–255)")
    plt.ylabel("Frekuensi")

    # Histogram hasil thresholding (hanya 0 & 255)
    plt.subplot(1,2,2)
    plt.title("Histogram Thresholding")
    counts, bins = np.histogram(Ko.flatten(), bins=[0,128,255])  
    plt.bar([0,255], counts, width=100, color="black", alpha=0.7)  
    plt.xticks([0,255])  
    plt.xlabel("Nilai Piksel (0=Hitam, 255=Putih)")
    plt.ylabel("Frekuensi")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
