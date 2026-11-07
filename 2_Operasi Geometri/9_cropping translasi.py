from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# ==============================
#   PROGRAM CROP + TRANSFORM
# ==============================

# --- INPUT GAMBAR ---
nama_file = input("Masukkan nama file gambar: ")

try:
    img = Image.open(nama_file)

    # Jika RGBA → ubah jadi background putih
    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg
    else:
        img = img.convert("RGB")

    w, h = img.size
    print(f"\nUkuran gambar: {w} x {h}")

    # --- INPUT KOORDINAT CROP ---
    print("\nMasukkan koordinat area crop:")
    xL = int(input("xL (kiri atas): "))
    yT = int(input("yT (kiri atas): "))
    xR = int(input("xR (kanan bawah): "))
    yB = int(input("yB (kanan bawah): "))

    # Validasi
    if xR <= xL or yB <= yT:
        print("❌ Koordinat crop tidak valid.")
        exit()

    # --- LAKUKAN CROP ---
    cropped = img.crop((xL, yT, xR, yB))

    # Ukuran hasil crop
    cw, ch = cropped.size
    print(f"\nUkuran hasil crop: {cw} x {ch}")

    # ============================
    #     PROSES TRANSFORMASI
    # ============================

    # Pisah menjadi 2 bagian
    top_h = ch // 2
    top = cropped.crop((0, 0, cw, top_h))      # bagian gedung
    bottom = cropped.crop((0, top_h, cw, ch))  # bagian biru

    # Rotasi top 90° CCW
    top_rot = top.rotate(90, expand=True)
    rw, rh = top_rot.size

    # Siapkan kanvas hasil akhir
    result = Image.new("RGB", (cw, ch), "white")

    # Posisi gedung (kanan bawah)
    x_pos = cw - rw
    y_pos = ch - rh

    # Tempel lapisan: gedung dahulu → biru di atas
    result.paste(top_rot, (x_pos, y_pos))  # bawah
    result.paste(bottom, (0, 0))           # atas

    # ============================
    #     TAMPILKAN HASIL
    # ============================

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Hasil Crop")
    plt.imshow(cropped)
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("Transformed")
    plt.imshow(result)
    plt.axis("off")

    plt.show()

    # Simpan hasil
    out_name = "hasil_transform_" + nama_file
    result.save(out_name)
    print("\nBerhasil! Hasil disimpan sebagai:", out_name)

except FileNotFoundError:
    print("File tidak ditemukan.")
