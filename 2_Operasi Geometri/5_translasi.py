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

    # Tampilkan informasi
    print("\n📌 Informasi Gambar:")
    print(f"- Format file     : {format_file}")
    print(f"- Mode warna      : {mode_warna}")
    print(f"- Resolusi        : {resolusi} piksel")
    print(f"- Kedalaman warna : {kedalaman} bit")
    print(f"- Rasio aspek     : {rasio_aspek}")
    print(f"- Ukuran file     : {ukuran_file} KB")

    # Konversi ke RGB agar seragam
    img = img.convert("RGB")

    # 3️⃣ Input jarak translasi
    print("\nMasukkan nilai translasi:")
    a = int(input("a (pergeseran horizontal, + = kanan, - = kiri): "))
    b = int(input("b (pergeseran vertikal, + = bawah, - = atas): "))

    # 4️⃣ Konversi gambar ke array
    img_array = np.array(img)
    h, w, c = img_array.shape

    # Buat array kosong untuk hasil translasi
    translated_array = np.zeros_like(img_array)

    # 5️⃣ Terapkan rumus translasi
    for y in range(h):
        for x in range(w):
            x_baru = x + a
            y_baru = y + b

            # Cek agar tidak keluar batas
            if 0 <= x_baru < w and 0 <= y_baru < h:
                translated_array[y_baru, x_baru] = img_array[y, x]

    # Konversi hasil ke gambar
    img_translated = Image.fromarray(translated_array)

    # 6️⃣ Simpan file TXT (informasi + rumus)
    txt_name = "hasil_translasi.txt"
    with open(txt_name, "w", encoding="utf-8") as f:
        f.write("Informasi Gambar:\n")
        f.write(f"- File        : {image_path}\n")
        f.write(f"- Format      : {format_file}\n")
        f.write(f"- Mode warna  : {mode_warna}\n")
        f.write(f"- Resolusi    : {resolusi}\n")
        f.write(f"- Kedalaman   : {kedalaman} bit\n")
        f.write(f"- Rasio aspek : {rasio_aspek}\n")
        f.write(f"- Translasi   : a = {a}, b = {b}\n\n")

        f.write("Rumus Translasi:\n")
        f.write("x' = x + a\n")
        f.write("y' = y + b\n\n")

        f.write("Transformasi titik:\n")
        for y in range(h):
            for x in range(w):
                x_baru = x + a
                y_baru = y + b
                if 0 <= x_baru < w and 0 <= y_baru < h:
                    f.write(f"f({y},{x}) → f'({y_baru},{x_baru})  "
                            f"dengan x' = {x}+{a}={x_baru}, y' = {y}+{b}={y_baru}\n")

    print(f"\n✅ Informasi translasi disimpan di: {txt_name}")

    # 7️⃣ Simpan file RGB transformasi
    rgb_name = "translasi_rgb.txt"
    with open(rgb_name, "w", encoding="utf-8") as f:
        f.write("Hasil Transformasi RGB setelah Translasi:\n\n")
        for y in range(h):
            for x in range(w):
                x_baru = x + a
                y_baru = y + b
                if 0 <= x_baru < w and 0 <= y_baru < h:
                    rgb_asli = img_array[y, x]
                    rgb_baru = translated_array[y_baru, x_baru]

                    f.write(
                        f"f({y},{x}) [R={rgb_asli[0]},G={rgb_asli[1]},B={rgb_asli[2]}] "
                        f"→ f'({y_baru},{x_baru}) [R={rgb_baru[0]},G={rgb_baru[1]},B={rgb_baru[2]}]\n"
                    )

    print(f"✅ Detail RGB disimpan di: {rgb_name}")

    # 8️⃣ Tampilkan hasil
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title(f"Translasi (a={a}, b={b})")
    plt.imshow(img_translated)
    plt.axis("off")

    plt.show()

if __name__ == "__main__":
    main()
