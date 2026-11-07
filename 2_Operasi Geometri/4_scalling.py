from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    # Input gambar
    image_path = input("Masukkan nama file gambar (misal: gambar.jpg): ")
    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print("❌ File tidak ditemukan.")
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

    # Input faktor skala
    Sh = float(input("Masukkan faktor skala horizontal (Sh): "))
    Sv = float(input("Masukkan faktor skala vertikal (Sv): "))

    # Konversi gambar ke array NumPy
    img_array = np.array(img)
    h, w, c = img_array.shape

    # Hitung ukuran baru
    w_new = int(w * Sh)
    h_new = int(h * Sv)
    scaled_array = np.zeros((h_new, w_new, c), dtype=np.uint8)

    # Scaling dengan replikasi piksel
    for y in range(h_new):
        for x in range(w_new):
            # cari koordinat asal (nearest neighbor)
            x_old = int(x / Sh)
            y_old = int(y / Sv)
            scaled_array[y, x] = img_array[y_old, x_old]

    # Konversi hasil scaling jadi gambar
    scaled_img = Image.fromarray(scaled_array)

    # Simpan perhitungan f(x,y) → f’(x’,y’) ke file
    with open("scaling_fx.txt", "w", encoding="utf-8") as f:
        f.write("Perhitungan f(x,y) -> f'(x',y'):\n\n")
        for y in range(h):
            for x in range(w):
                for dy in range(int(Sv)):
                    for dx in range(int(Sh)):
                        x_new = int(x * Sh) + dx
                        y_new = int(y * Sv) + dy
                        f.write(f"f({y},{x}) -> f'({y_new},{x_new})\n")

    # Simpan transformasi RGB f(x,y) -> f'(x’,y’)
    with open("scaling_rgb.txt", "w", encoding="utf-8") as f:
        f.write("Transformasi nilai RGB:\n\n")
        for y in range(h):
            for x in range(w):
                rgb = img_array[y, x]
                for dy in range(int(Sv)):
                    for dx in range(int(Sh)):
                        x_new = int(x * Sh) + dx
                        y_new = int(y * Sv) + dy
                        f.write(f"f({y},{x})[RGB={tuple(rgb)}] "
                                f"-> f'({y_new},{x_new})[RGB={tuple(rgb)}]\n")

    print("\n✅ Hasil scaling berhasil disimpan di scaling_fx.txt dan scaling_rgb.txt")

    # Tampilkan gambar asli & hasil scaling
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title(f"Hasil Scaling (Sh={Sh}, Sv={Sv})")
    plt.imshow(scaled_img)
    plt.axis("off")

    plt.show()

if __name__ == "__main__":
    main()
