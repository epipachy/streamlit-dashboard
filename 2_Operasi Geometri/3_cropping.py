from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    # 1️⃣ Input gambar
    image_path = input("Masukkan nama gambar: ")
    try:
        img = Image.open(image_path).convert("RGB")
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

    # Ambil ukuran gambar
    h, w = img.height, img.width
    img_array = np.array(img)

    print(f"\nUkuran gambar asli: {w} x {h}")
    print("Masukkan koordinat crop (xL,yT) dan (xR,yB):")

    # 2️⃣ Input koordinat crop
    xL = int(input("xL (pojok kiri atas): "))
    yT = int(input("yT (pojok kiri atas): "))
    xR = int(input("xR (pojok kanan bawah): "))
    yB = int(input("yB (pojok kanan bawah): "))

    # 3️⃣ Hitung ukuran gambar hasil crop
    w_new = xR - xL
    h_new = yB - yT

    if w_new <= 0 or h_new <= 0:
        print("❌ Koordinat crop tidak valid.")
        return

    cropped_array = np.zeros((h_new, w_new, 3), dtype=np.uint8)

    # 4️⃣ Simpan hasil perhitungan ke 2 file
    txt_rumus = "hasil_crop.txt"
    txt_rgb = "crop_rgb.txt"

    with open(txt_rumus, "w", encoding="utf-8") as f_rumus, open(txt_rgb, "w", encoding="utf-8") as f_rgb:
        f_rumus.write("Hasil Transformasi Koordinat Crop:\n\n")
        f_rgb.write("Hasil Transformasi RGB setelah Crop:\n\n")

        for y in range(yT, yB):
            for x in range(xL, xR):
                # Rumus koordinat
                x_new = x - xL
                y_new = y - yT
                rumus = f"x' = {x}-{xL} = {x_new}, y' = {y}-{yT} = {y_new}"

                # Simpan piksel ke citra hasil
                cropped_array[y_new, x_new] = img_array[y, x]

                # RGB asli dan baru
                rgb_asli = img_array[y, x]
                rgb_baru = cropped_array[y_new, x_new]

                f_rumus.write(f"f({y},{x}) → f'({y_new},{x_new}) dengan {rumus}\n")
                f_rgb.write(
                    f"f({y},{x}) [R={rgb_asli[0]},G={rgb_asli[1]},B={rgb_asli[2]}] "
                    f"→ f'({y_new},{x_new}) [R={rgb_baru[0]},G={rgb_baru[1]},B={rgb_baru[2]}]\n"
                )

    print(f"\n✅ Hasil rumus koordinat disimpan di {txt_rumus}")
    print(f"✅ Hasil transformasi RGB disimpan di {txt_rgb}")

    # 5️⃣ Konversi hasil crop ke gambar & tampilkan
    img_cropped = Image.fromarray(cropped_array)
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.title("Hasil Crop")
    plt.imshow(img_cropped)
    plt.axis("off")

    plt.show()

if __name__ == "__main__":
    main()