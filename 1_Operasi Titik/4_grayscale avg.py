from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def main():
    # 1️⃣ Input gambar
    image_path = input("Masukkan nama gambar: ")
    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    # 2️⃣ Konversi ke array NumPy
    img_array = np.array(img, dtype=np.float32)

    # Rumus Gray = (R + G + B) / 3
    gray_array = (img_array[:,:,0] + img_array[:,:,1] + img_array[:,:,2]) / 3
    gray_array = np.clip(gray_array, 0, 255).astype(np.uint8)

    # 3️⃣ Simpan semua nilai f(x,y) ke file .txt (dengan rumusnya)
    txt_name = "hasil_grayscale_avg.txt"
    with open(txt_name, "w") as f:
        h, w = gray_array.shape
        f.write(f"Gambar: {image_path}\nUkuran: {h} x {w}\nOperasi: Konversi ke Grayscale (Average)\n\n")
        for y in range(h):
            for x in range(w):
                R, G, B = img_array[y, x]
                gray_val = gray_array[y, x]
                f.write(
                    f"f({y},{x}) = ({int(R)} + {int(G)} + {int(B)}) / 3 = {gray_val}\n"
                )

    print(f"\n✅ Semua nilai f(x,y) dengan rumus sudah disimpan di file: {txt_name}")

    # 4️⃣ Konversi hasil kembali ke gambar
    img_gray = Image.fromarray(gray_array)

    # 5️⃣ Tampilkan gambar asli & grayscale
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Gambar Asli (RGB)")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.title("Gambar Grayscale (Average)")
    plt.imshow(img_gray, cmap="gray")
    plt.axis("off")

    plt.show()

    # 6️⃣ Histogram
    plt.figure(figsize=(6,4))
    plt.title("Histogram Grayscale (Average)")
    plt.hist(gray_array.flatten(), bins=256, range=(0,256), color="gray", alpha=0.7)
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Frekuensi")
    plt.show()

if __name__ == "__main__":
    main()
