from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os  # supaya bisa cek ukuran file

def main():
    # 1️⃣ Input gambar
    image_path = input("Masukkan nama gambar: ")
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    # 🔍 Pastikan mode RGB atau L (grayscale)
    if img.mode not in ["RGB", "L"]:
        img = img.convert("RGB")

    # ✅ Ambil informasi gambar
    format_file = img.format if img.format else os.path.splitext(image_path)[1].upper()
    mode_warna = img.mode
    resolusi = img.size  # (lebar, tinggi)
    kedalaman = len(img.getbands()) * 8  # contoh: RGB = 3x8 = 24 bit
    rasio_aspek = round(resolusi[0] / resolusi[1], 2)
    ukuran_file = round(os.path.getsize(image_path) / 1024, 2)  # KB

    # ✅ Tampilkan informasi di terminal
    print("\n📌 Informasi Gambar:")
    print(f"- Format file     : {format_file}")
    print(f"- Mode warna      : {mode_warna}")
    print(f"- Resolusi        : {resolusi} piksel")
    print(f"- Kedalaman warna : {kedalaman} bit (per piksel)")
    print(f"- Rasio aspek     : {rasio_aspek} (lebar/tinggi)")
    print(f"- Ukuran file     : {ukuran_file} KB")

    # 2️⃣ Input konstanta C
    C = int(input("\nMasukkan nilai konstanta C: "))

    # 3️⃣ Ubah ke array NumPy
    img_array = np.array(img, dtype=np.int16)  # supaya tidak overflow
    img_bright_array = np.clip(img_array + C, 0, 255).astype(np.uint8)  # Ko = Ki + C

    # 4️⃣ Simpan semua nilai f(x,y) ke file .txt
    txt_name = "hasil_brightness.txt"
    with open(txt_name, "w") as f:
        h, w = img_array.shape[:2]
        f.write(f"Gambar: {image_path}\nUkuran: {h} x {w}\nKonstanta C: {C}\n\n")
        for y in range(h):
            for x in range(w):
                f.write(f"f({x},{y}) = {img_array[y,x]} + {C} -> {img_bright_array[y,x]}\n")

    print(f"\n✅ Semua nilai f(x,y) sudah disimpan di file: {txt_name}")

    # 5️⃣ Konversi hasil kembali ke gambar
    img_bright = Image.fromarray(img_bright_array)

    # 6️⃣ Tampilkan gambar asli & hasil brightness
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Gambar Asli")
    plt.imshow(img, cmap="gray" if mode_warna == "L" else None)
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.title(f"Gambar + {C}")
    plt.imshow(img_bright, cmap="gray" if mode_warna == "L" else None)
    plt.axis("off")

    plt.show()

    # 7️⃣ Histogram
    if len(img_array.shape) == 2:
        # 🔹 Grayscale
        plt.figure(figsize=(8,4))
        plt.subplot(1,2,1)
        plt.title("Histogram Asli (Grayscale)")
        plt.hist(img_array.flatten(), bins=256, range=(0,256), color='gray', alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")

        plt.subplot(1,2,2)
        plt.title(f"Histogram + {C} (Grayscale)")
        plt.hist(img_bright_array.flatten(), bins=256, range=(0,256), color='gray', alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")
        plt.tight_layout()
        plt.show()
    else:
        # 🔹 RGB
        colors = ('red', 'green', 'blue')
        channel_labels = ('R', 'G', 'B')

        y_max = 0
        for i in range(3):
            hist_asli, _ = np.histogram(img_array[:,:,i].flatten(), bins=256, range=(0,256))
            hist_bright, _ = np.histogram(img_bright_array[:,:,i].flatten(), bins=256, range=(0,256))
            y_max = max(y_max, hist_asli.max(), hist_bright.max())

        y_limit = int(y_max * 0.2)  # ambil 20% dari maksimum

        plt.figure(figsize=(12,6))
        for i, color in enumerate(colors):
            plt.subplot(2,3,i+1)
            plt.title(f"Histogram {channel_labels[i]} Asli")
            plt.hist(img_array[:,:,i].flatten(), bins=256, range=(0,256), color=color, alpha=0.7)
            plt.xlabel("Intensitas Piksel")
            plt.ylabel("Frekuensi")
            plt.ylim(0, y_limit)

            plt.subplot(2,3,i+4)
            plt.title(f"Histogram {channel_labels[i]} + {C}")
            plt.hist(img_bright_array[:,:,i].flatten(), bins=256, range=(0,256), color=color, alpha=0.7)
            plt.xlabel("Intensitas Piksel")
            plt.ylabel("Frekuensi")
            plt.ylim(0, y_limit)

        plt.tight_layout()
        plt.show()

# ✅ Jalankan
if __name__ == "__main__":
    main()
