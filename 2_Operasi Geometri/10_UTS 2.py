from PIL import Image
import matplotlib.pyplot as plt

# --- INPUT GAMBAR ---
nama_file = input("Masukkan nama file gambar: ")

try:
    img = Image.open(nama_file)

    # === Jika gambar punya transparansi (RGBA), jadikan background putih ===
    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])  # gunakan alpha sebagai mask
        img = bg
    else:
        img = img.convert("RGB")

    w, h = img.size

    # --- Pisahkan gambar jadi 2 bagian ---
    top_h = h // 2
    top = img.crop((0, 0, w, top_h))      # gambar gedung
    bottom = img.crop((0, top_h, w, h))   # gambar biru

    # --- ROTASI 90° COUNTER-CLOCKWISE ---
    top_rot = top.rotate(90, expand=True)

    # --- Siapkan kanvas hasil ---
    result = Image.new("RGB", (w, h), "white")

    # Hitung posisi gedung (kanan–bawah)
    rw, rh = top_rot.size
    x_pos = w - rw
    y_pos = h - rh

    # 1️⃣ Tempel GEDUNG DULU (lapisan bawah)
    result.paste(top_rot, (x_pos, y_pos))

    # 2️⃣ Tempel BIRU DI ATASNYA (lapisan atas)
    result.paste(bottom, (0, 0))

    # --- TAMPILKAN PERBANDINGAN ---
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Transformed")
    plt.imshow(result)
    plt.axis("off")

    plt.show()

    # --- SIMPAN HASIL ---
    out_name = "hasil_" + nama_file
    result.save(out_name)
    print("Berhasil! Hasil disimpan sebagai:", out_name)

except FileNotFoundError:
    print("File tidak ditemukan.")