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

    # ✅ Tampilkan informasi di terminal
    print("\n📌 Informasi Gambar:")
    print(f"- Format file     : {format_file}")
    print(f"- Mode warna      : {mode_warna}")
    print(f"- Resolusi        : {resolusi} piksel")
    print(f"- Kedalaman warna : {kedalaman} bit (per piksel)")
    print(f"- Rasio aspek     : {rasio_aspek} (lebar/tinggi)")
    print(f"- Ukuran file     : {ukuran_file} KB")

    # Konversi ke RGB agar seragam
    img = img.convert("RGB")

    # 3️⃣ Pilih jenis flipping
    print("\nPilih jenis flipping:")
    print("1. Horizontal")
    print("2. Vertikal")
    print("3. Kombinasi (Horizontal + Vertikal)")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    # 4️⃣ Konversi ke array NumPy
    img_array = np.array(img)
    h, w, c = img_array.shape
    flipped_array = np.zeros_like(img_array)

    # 🔁 Terapkan rumus pencerminan
    for y in range(h):
        for x in range(w):
            if pilihan == "1":  # Horizontal
                x_baru = w - 1 - x
                y_baru = y
            elif pilihan == "2":  # Vertikal
                x_baru = x
                y_baru = h - 1 - y
            elif pilihan == "3":  # Kombinasi
                x_baru = w - 1 - x
                y_baru = h - 1 - y
            else:
                print("Pilihan tidak valid.")
                return

            flipped_array[y_baru, x_baru] = img_array[y, x]

    # Konversi hasil ke gambar
    img_flipped = Image.fromarray(flipped_array)

    # 5️⃣ Simpan informasi gambar & rumus flipping ke file .txt
    txt_name = "hasil_flipping.txt"
    with open(txt_name, "w", encoding="utf-8") as f:
        f.write("Informasi Gambar:\n")
        f.write(f"- File        : {image_path}\n")
        f.write(f"- Format      : {format_file}\n")
        f.write(f"- Mode warna  : {mode_warna}\n")
        f.write(f"- Resolusi    : {resolusi} piksel\n")
        f.write(f"- Kedalaman   : {kedalaman} bit (per piksel)\n")
        f.write(f"- Rasio aspek : {rasio_aspek}\n")
        f.write(f"- Ukuran file : {ukuran_file} KB\n")
        f.write(f"- Jenis Flip  : {pilihan}\n\n")

        for y in range(h):
            for x in range(w):
                if pilihan == "1":  # Horizontal
                    x_baru = w - 1 - x
                    y_baru = y
                    rumus = f"x' = {w}-1-{x} = {x_baru}, y' = {y}"
                elif pilihan == "2":  # Vertikal
                    x_baru = x
                    y_baru = h - 1 - y
                    rumus = f"x' = {x}, y' = {h}-1-{y} = {y_baru}"
                else:  # Kombinasi
                    x_baru = w - 1 - x
                    y_baru = h - 1 - y
                    rumus = f"x' = {w}-1-{x} = {x_baru}, y' = {h}-1-{y} = {y_baru}"
                f.write(f"f({y},{x}) → f'({y_baru},{x_baru}) dengan {rumus}\n")

    print(f"\n✅ Informasi gambar & hasil flipping sudah disimpan di file: {txt_name}")

    # 6️⃣ Buat file baru untuk hasil transformasi nilai RGB
    rgb_file = "flipping_rgb.txt"
    with open(rgb_file, "w", encoding="utf-8") as f:
        f.write("Hasil Transformasi Nilai RGB setelah Flipping:\n\n")
        for y in range(h):
            for x in range(w):
                if pilihan == "1":
                    x_baru = w - 1 - x
                    y_baru = y
                elif pilihan == "2":
                    x_baru = x
                    y_baru = h - 1 - y
                else:
                    x_baru = w - 1 - x
                    y_baru = h - 1 - y

                rgb_asli = img_array[y, x]
                rgb_baru = flipped_array[y_baru, x_baru]

                f.write(
                    f"f({y},{x}) [R={rgb_asli[0]},G={rgb_asli[1]},B={rgb_asli[2]}] "
                    f"→ f'({y_baru},{x_baru}) [R={rgb_baru[0]},G={rgb_baru[1]},B={rgb_baru[2]}]\n"
                )

    print(f"✅ Detail transformasi RGB sudah disimpan di file: {rgb_file}")

    # 7️⃣ Tampilkan gambar asli & hasil flipping
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,2,2)
    if pilihan == "1":
        plt.title("Flipping Horizontal")
    elif pilihan == "2":
        plt.title("Flipping Vertikal")
    else:
        plt.title("Flipping Kombinasi")
    plt.imshow(img_flipped)
    plt.axis("off")

    plt.show()

if __name__ == "__main__":
    main()