from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    # 1️⃣ Input gambar
    image_path = input("Masukkan nama gambar: ")
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    # 2️⃣ Ambil informasi dasar gambar
    format_file = img.format
    mode_warna = img.mode
    resolusi = f"{img.width} x {img.height}"
    kedalaman = len(img.getbands()) * 8
    rasio_aspek = round(img.width / img.height, 2)
    ukuran_file = round(os.path.getsize(image_path) / 1024, 2)  # KB

    # ✅ Tampilkan informasi di terminal (boleh pakai emoji)
    print("\n📌 Informasi Gambar:")
    print(f"- Format file     : {format_file}")
    print(f"- Mode warna      : {mode_warna}")
    print(f"- Resolusi        : {resolusi} piksel")
    print(f"- Kedalaman warna : {kedalaman} bit (per piksel)")
    print(f"- Rasio aspek     : {rasio_aspek} (lebar/tinggi)")
    print(f"- Ukuran file     : {ukuran_file} KB")

    # Konversi ke RGB agar seragam
    img = img.convert("RGB")

    # 3️⃣ Input faktor kontras (G)
    G = float(input("\nMasukkan faktor kontras (misal 1.5 = lebih kontras, 0.8 = lebih rendah): "))

    # 4️⃣ Konversi ke array NumPy
    img_array = np.array(img, dtype=np.int16)
    P = 128  # titik pusat kontras

    # Rumus: Ko = G * (Ki - P) + P
    img_contrast_array = np.clip(G * (img_array - P) + P, 0, 255).astype(np.uint8)

    # 5️⃣ Simpan informasi gambar & semua nilai f(x,y) ke file .txt (tanpa emoji)
    txt_name = "hasil_kontras.txt"
    with open(txt_name, "w", encoding="utf-8") as f:
        f.write("Informasi Gambar:\n")
        f.write(f"- File           : {image_path}\n")
        f.write(f"- Format         : {format_file}\n")
        f.write(f"- Mode warna     : {mode_warna}\n")
        f.write(f"- Resolusi       : {resolusi} piksel\n")
        f.write(f"- Kedalaman      : {kedalaman} bit (per piksel)\n")
        f.write(f"- Rasio aspek    : {rasio_aspek}\n")
        f.write(f"- Ukuran file    : {ukuran_file} KB\n")
        f.write(f"- Faktor Kontras : {G}\n\n")

        h, w, c = img_array.shape
        for y in range(h):
            for x in range(w):
                for ch, ch_name in enumerate(["R","G","B"]):
                    Ki = img_array[y, x, ch]
                    Ko = img_contrast_array[y, x, ch]
                    rumus = f"{G} * ({Ki} - {P}) + {P}"
                    f.write(f"f({y},{x})[{ch_name}] = {rumus} = {Ko}\n")

    print(f"\n✅ Informasi gambar & semua nilai f(x,y) sudah disimpan di file: {txt_name}")

    # 6️⃣ Konversi hasil kembali ke gambar
    img_contrast = Image.fromarray(img_contrast_array)

    # 7️⃣ Tampilkan gambar asli & hasil kontras
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.title(f"Kontras (G={G})")
    plt.imshow(img_contrast)
    plt.axis("off")

    plt.show()

    # 8️⃣ Histogram per channel (RGB) dengan skala sama
    colors = ('red', 'green', 'blue')
    channel_labels = ('R', 'G', 'B')

    # Cari maksimum frekuensi histogram biar skala sama
    y_max = 0
    for i in range(3):
        hist_asli, _ = np.histogram(img_array[:,:,i].flatten(), bins=256, range=(0,256))
        hist_kontras, _ = np.histogram(img_contrast_array[:,:,i].flatten(), bins=256, range=(0,256))
        y_max = max(y_max, hist_asli.max(), hist_kontras.max())

    # 🔽 Perkecil skala (misalnya hanya 20% dari puncak maksimum)
    y_limit = int(y_max * 0.2)

    plt.figure(figsize=(12,6))
    for i, color in enumerate(colors):
        plt.subplot(2,3,i+1)
        plt.title(f"Histogram {channel_labels[i]} Asli")
        plt.hist(img_array[:,:,i].flatten(), bins=256, range=(0,256), color=color, alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")
        plt.ylim(0, y_limit)

        plt.subplot(2,3,i+4)
        plt.title(f"Histogram {channel_labels[i]} Kontras")
        plt.hist(img_contrast_array[:,:,i].flatten(), bins=256, range=(0,256), color=color, alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")
        plt.ylim(0, y_limit)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()