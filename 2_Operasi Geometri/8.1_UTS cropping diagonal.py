from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# =========================
#       FUNGSI CROP
# =========================

def crop_diagonal(img_array):
    h, w, _ = img_array.shape
    cropped_array = np.ones_like(img_array) * 255  # background putih

    for y in range(h):
        for x in range(w):
            batas = (w - x - 1) * h / w  # garis diagonal
            if y <= batas:              # tampilkan bagian atas diagonal
                cropped_array[y, x] = img_array[y, x]

    return cropped_array


# =========================
#         MAIN APP
# =========================

def main():
    # 1️⃣ Input gambar
    image_path = input("Masukkan nama gambar: ")
    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    img_array = np.array(img)
    h, w = img_array.shape[:2]

    # Informasi dasar
    format_file = img.format if img.format else "N/A"
    mode_warna = img.mode
    resolusi = f"{img.width} x {img.height}"
    kedalaman = len(img.getbands()) * 8
    rasio_aspek = round(img.width / img.height, 2)
    ukuran_file = round(os.path.getsize(image_path) / 1024, 2)

    # ======================
    #   AUTO CROP DIAGONAL
    # ======================

    cropped_array = crop_diagonal(img_array)
    img_cropped = Image.fromarray(cropped_array)
    crop_desc = "Diagonal Atas"
    title_crop = "Crop Diagonal (Atas)"

    # ======================
    #   AUTO FLIP KOMBINASI
    # ======================

    flip_h, flip_w = cropped_array.shape[:2]
    flipped_array = np.zeros_like(cropped_array)

    for y in range(flip_h):
        for x in range(flip_w):
            x_baru = flip_w - 1 - x
            y_baru = flip_h - 1 - y
            flipped_array[y_baru, x_baru] = cropped_array[y, x]

    img_flipped = Image.fromarray(flipped_array)
    flip_name = "Flipping Kombinasi (H+V)"

    # ======================
    #      TXT FILE 1
    # ======================

    txt_info = "hasil_transformasi.txt"
    with open(txt_info, "w", encoding="utf-8") as f:
        f.write("Informasi Gambar Asli:\n")
        f.write(f"- File        : {image_path}\n")
        f.write(f"- Format      : {format_file}\n")
        f.write(f"- Mode warna  : {mode_warna}\n")
        f.write(f"- Resolusi    : {resolusi}\n")
        f.write(f"- Kedalaman   : {kedalaman} bit\n")
        f.write(f"- Rasio aspek : {rasio_aspek}\n")
        f.write(f"- Ukuran file : {ukuran_file} KB\n\n")

        f.write(f"Mode Crop     : {crop_desc}\n")
        f.write(f"Mode Flipping : {flip_name}\n\n")

        f.write("Transformasi Koordinat:\n")

        for y in range(flip_h):
            for x in range(flip_w):
                x_baru = flip_w - 1 - x
                y_baru = flip_h - 1 - y
                rumus = f"x' = {flip_w}-1-{x}, y' = {flip_h}-1-{y}"
                f.write(f"({y},{x}) → ({y_baru},{x_baru}) | {rumus}\n")

    print(f"\n📄 TXT 1 disimpan: {txt_info}")

    # ======================
    #      TXT FILE 2
    # ======================

    txt_rgb = "rgb_transformasi.txt"
    with open(txt_rgb, "w", encoding="utf-8") as f:
        f.write("Perubahan Nilai RGB Setelah Transformasi:\n\n")

        for y in range(flip_h):
            for x in range(flip_w):
                x_baru = flip_w - 1 - x
                y_baru = flip_h - 1 - y
                rgb_asli = cropped_array[y, x]
                rgb_baru = flipped_array[y_baru, x_baru]

                f.write(
                    f"({y},{x}) [R={rgb_asli[0]},G={rgb_asli[1]},B={rgb_asli[2]}] → "
                    f"({y_baru},{x_baru}) [R={rgb_baru[0]},G={rgb_baru[1]},B={rgb_baru[2]}]\n"
                )

    print(f"📄 TXT 2 disimpan: {txt_rgb}")

    # ======================
    #      TAMPILKAN
    # ======================

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title(title_crop)
    plt.imshow(img_cropped)
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title(flip_name)
    plt.imshow(img_flipped)
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
