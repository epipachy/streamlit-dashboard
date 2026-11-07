from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# ==============================
# 📊 Fungsi Histogram
# ==============================
def tampilkan_histogram_per_gambar(arrA, arrB, arrC):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    datasets = [(arrA, 'Histogram Gambar A'),
                (arrB, 'Histogram Gambar B'),
                (arrC, 'Histogram Hasil Blending')]
    colors = ['r', 'g', 'b']

    max_y = 0
    for arr in [arrA, arrB, arrC]:
        for i in range(3):
            hist, _ = np.histogram(arr[:, :, i].ravel(), bins=256)
            max_y = max(max_y, hist.max())

    for idx, (arr, title) in enumerate(datasets):
        axes[idx].set_title(title)
        axes[idx].set_xlabel("Intensitas (0-255)")
        axes[idx].set_ylabel("Jumlah Piksel")
        for i, color in enumerate(colors):
            axes[idx].hist(
                arr[:, :, i].ravel(),
                bins=256,
                color=color,
                alpha=0.4,
                label=color.upper(),
                edgecolor=color,
                linewidth=0.8
            )
        axes[idx].legend()
        axes[idx].grid(True, linestyle='--', alpha=0.3)
        axes[idx].set_ylim(0, max_y*1.05)
    plt.tight_layout()
    plt.show()

# ==============================
# 📝 Fungsi Info Gambar
# ==============================
def tampilkan_info_gambar(image_path, img_obj, label):
    format_file = img_obj.format or os.path.splitext(image_path)[1].upper().replace('.', '')
    mode_warna = img_obj.mode
    resolusi = f"{img_obj.width} x {img_obj.height}"
    kedalaman = len(img_obj.getbands()) * 8
    rasio_aspek = round(img_obj.width / img_obj.height, 2)
    ukuran_file = round(os.path.getsize(image_path) / 1024, 2)

    print(f"\n📌 Informasi {label}:")
    print(f"- Format file     : {format_file}")
    print(f"- Mode warna      : {mode_warna}")
    print(f"- Resolusi        : {resolusi}")
    print(f"- Kedalaman warna : {kedalaman} bit")
    print(f"- Rasio aspek     : {rasio_aspek}")
    print(f"- Ukuran file     : {ukuran_file} KB")

# ==============================
# 🖼 Fungsi Tampilkan Gambar
# ==============================
def tampilkan_gambar_layout(imgA, imgB_preview, blended_img):
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_title("Gambar A")
    ax1.imshow(imgA)
    ax1.axis("off")

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.set_title("Gambar B")
    ax2.imshow(imgB_preview)
    ax2.axis("off")

    ax3 = fig.add_subplot(2, 1, 2)
    ax3.set_title("Hasil Blending")
    ax3.imshow(blended_img)
    ax3.axis("off")

    plt.tight_layout()
    plt.show()

# ==============================
# 🧮 Fungsi Resize + Crop dari Ujung Kiri-Atas
# ==============================
def resize_crop_from_top_left(img, target_width, target_height):
    ratio_target = target_width / target_height # rasio target = rasio yang kita mau (gambar a)
    ratio_img = img.width / img.height # rasio img = rasio yang belum diapa-apain (gambar b)

    if ratio_img > ratio_target: #jika gambar b lebih besar dr yang dibutuhkan, maka:
        # terlalu lebar → resize tinggi, crop lebar
        new_height = target_height #samakan tingginya dulu 
        new_width = int(img.width * (new_height / img.height))
    else:
        # terlalu tinggi → resize lebar, crop tinggi
        new_width = target_width
        new_height = int(img.height * (new_width / img.width))

    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    img_cropped = img_resized.crop((0, 0, target_width, target_height))  # crop dari kiri-atas
    return img_cropped

# ==============================
# 🧮 MAIN PROGRAM
# ==============================
def main():
    print("=== 📸 Program Penggabungan Citra (Image Blending) ===")

    imageA_path = input("Masukkan nama gambar A: ")
    imageB_path = input("Masukkan nama gambar B: ")

    try:
        imgA = Image.open(imageA_path).convert("RGB")
        imgB = Image.open(imageB_path).convert("RGB")
    except FileNotFoundError:
        print("❌ Salah satu file gambar tidak ditemukan.")
        return

    # Simpan gambar B asli untuk preview
    imgB_asli = imgB.copy()

    # Resize + Crop sementara untuk blending
    imgB_for_blend = resize_crop_from_top_left(imgB, imgA.width, imgA.height)

    tampilkan_info_gambar(imageA_path, imgA, "Gambar A")
    tampilkan_info_gambar(imageB_path, imgB, "Gambar B")

    # Input bobot
    wa = float(input("\nMasukkan bobot untuk gambar A (misal 0.4): "))
    wb = float(input("Masukkan bobot untuk gambar B (misal 0.6): "))
    if round(wa + wb, 2) != 1.0:
        print("❌ Jumlah bobot wa + wb harus = 1.")
        return

    # Konversi ke array
    arrA = np.array(imgA, dtype=np.float32)
    arrB = np.array(imgB_for_blend, dtype=np.float32)

    # Operasi blending
    blended_array = wa * arrA + wb * arrB
    blended_array = np.clip(blended_array, 0, 255).astype(np.uint8)
    blended_img = Image.fromarray(blended_array)

    # Simpan hasil perhitungan pixel
    with open("hasil_blending.txt", "w", encoding="utf-8") as f:
        f.write(f"Blending Citra:\nC(x,y) = {wa}*A(x,y) + {wb}*B(x,y)\n")
        tinggi, lebar, _ = arrA.shape
        for y in range(tinggi):
            for x in range(lebar):
                A_pixel = arrA[y, x].astype(int)
                B_pixel = arrB[y, x].astype(int)
                C_pixel = blended_array[y, x].astype(int)
                f.write(f"C({x},{y}) = {wa}{A_pixel.tolist()} + {wb}{B_pixel.tolist()} = {C_pixel.tolist()}\n")

    print("✅ Semua perhitungan blending disimpan di: hasil_blending.txt")

    # Tampilkan gambar & histogram (preview tetap gambar asli)
    tampilkan_gambar_layout(imgA, imgB_asli, blended_img)
    tampilkan_histogram_per_gambar(arrA, arrB, blended_array)

    # Simpan hasil blending
    blended_img.save("hasil_blending.jpg")
    print("💾 Hasil blending disimpan sebagai: hasil_blending.jpg")

# ==============================
if __name__ == "__main__":
    main()