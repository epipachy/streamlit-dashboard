from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
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

    # 2️⃣ Pilih jenis rotasi
    print("\nPilih jenis rotasi:")
    print("1. Rotasi 90° CW")
    print("2. Rotasi 180° CW")
    print("3. Rotasi Bebas (CCW)")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    # Tentukan ukuran gambar baru
    if pilihan == "1":  # 90° CW
        w_new, h_new = h, w
        rotated_array = np.zeros((h_new, w_new, 3), dtype=np.uint8)
    elif pilihan == "2":  # 180° CW
        w_new, h_new = w, h
        rotated_array = np.zeros((h_new, w_new, 3), dtype=np.uint8)
    elif pilihan == "3":  # Rotasi bebas
        theta_deg = float(input("Masukkan sudut rotasi (derajat): "))
        theta = math.radians(theta_deg)
        w_new = int(abs(w * math.cos(theta)) + abs(h * math.sin(theta)))
        h_new = int(abs(w * math.sin(theta)) + abs(h * math.cos(theta)))
        
        # 🟢 Background putih
        rotated_array = np.full((h_new, w_new, 3), 255, dtype=np.uint8)
    else:
        print("Pilihan tidak valid.")
        return

    # 3️⃣ Proses rotasi + simpan hasil ke file (proses hitungan)
    txt_rumus = "proses_koordinat.txt"
    txt_rgb = "proses_rgb.txt"

    with open(txt_rumus, "w", encoding="utf-8") as f_rumus, open(txt_rgb, "w", encoding="utf-8") as f_rgb:
        f_rumus.write("Proses Perhitungan Transformasi Koordinat Rotasi:\n\n")
        f_rgb.write("Proses Perhitungan Transformasi RGB:\n\n")

        if pilihan in ["1", "2"]:
            for y in range(h):
                for x in range(w):
                    if pilihan == "1":  # 90° CW
                        x_new = h - 1 - y
                        y_new = x
                        rumus = f"x' = h-1-y = {h}-1-{y} = {x_new}, y' = x = {x} → y' = {y_new}"
                    elif pilihan == "2":  # 180° CW
                        x_new = w - 1 - x
                        y_new = h - 1 - y
                        rumus = f"x' = w-1-x = {w}-1-{x} = {x_new}, y' = h-1-y = {h}-1-{y} = {y_new}"

                    rotated_array[y_new, x_new] = img_array[y, x]

                    rgb_asli = img_array[y, x]
                    rgb_baru = rotated_array[y_new, x_new]

                    f_rumus.write(
                        f"Koordinat asli f({y},{x}) → f'({y_new},{x_new}) | {rumus}\n"
                    )

                    f_rgb.write(
                        f"RGB asli f({y},{x}) [R={rgb_asli[0]},G={rgb_asli[1]},B={rgb_asli[2]}] "
                        f"→ RGB baru f'({y_new},{x_new}) = img_array[{y},{x}] = {rgb_baru.tolist()}\n"
                    )

        elif pilihan == "3":  # Rotasi bebas (inverse mapping + proses hitungan detail)
            x_center, y_center = w / 2, h / 2
            x_new_center, y_new_center = w_new / 2, h_new / 2

            for y_new in range(h_new):
                for x_new in range(w_new):
                    x_rel_new = x_new - x_new_center
                    y_rel_new = y_new - y_new_center

                    # inverse mapping ke koordinat asli
                    x_old_float = x_rel_new * math.cos(-theta) + y_rel_new * math.sin(-theta) + x_center
                    y_old_float = -x_rel_new * math.sin(-theta) + y_rel_new * math.cos(-theta) + y_center
                    x_old = int(x_old_float)
                    y_old = int(y_old_float)

                    if 0 <= x_old < w and 0 <= y_old < h:
                        rotated_array[y_new, x_new] = img_array[y_old, x_old]
                        rgb_asli = img_array[y_old, x_old]
                        rgb_baru = rotated_array[y_new, x_new]

                        # Tulis proses perhitungan koordinat
                        f_rumus.write(
                            f"x_new={x_new}, y_new={y_new}\n"
                            f"  x_rel_new = x_new - x_new_center = {x_new} - {x_new_center:.2f} = {x_rel_new:.2f}\n"
                            f"  y_rel_new = y_new - y_new_center = {y_new} - {y_new_center:.2f} = {y_rel_new:.2f}\n"
                            f"  x_old_float = x_rel_new*cos(-θ) + y_rel_new*sin(-θ) + x_center = {x_old_float:.2f}\n"
                            f"  y_old_float = -x_rel_new*sin(-θ) + y_rel_new*cos(-θ) + y_center = {y_old_float:.2f}\n"
                            f"  x_old = int({x_old_float:.2f}) = {x_old}, y_old = int({y_old_float:.2f}) = {y_old}\n\n"
                        )

                        # Tulis proses perhitungan RGB
                        f_rgb.write(
                            f"RGB asli f({y_old},{x_old}) [R={rgb_asli[0]},G={rgb_asli[1]},B={rgb_asli[2]}] "
                            f"→ RGB baru f'({y_new},{x_new}) = img_array[{y_old},{x_old}] = {rgb_baru.tolist()}\n\n"
                        )

    print(f"\n✅ Proses koordinat disimpan di {txt_rumus}")
    print(f"✅ Proses transformasi RGB disimpan di {txt_rgb}")

    # 4️⃣ Konversi ke gambar & tampilkan
    img_rotated = Image.fromarray(rotated_array)
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,2,2)
    if pilihan == "1":
        plt.title("Rotasi 90° CW")
    elif pilihan == "2":
        plt.title("Rotasi 180° CW")
    else:
        plt.title(f"Rotasi Bebas (θ={theta_deg:.1f}° CCW)")
    plt.imshow(img_rotated)
    plt.axis("off")

    plt.show()

if __name__ == "__main__":
    main()
