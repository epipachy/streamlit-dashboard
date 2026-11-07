from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    # Input gambar
    image_path = input("Masukkan nama gambar: ")
    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    # Info gambar
    h, w = img.height, img.width
    img_array = np.array(img)

    # Crop diagonal (ambil bagian atas)
    Y, X = np.ogrid[:h, :w]
    mask = Y <= (h / w) * X
    cropped_array = np.zeros_like(img_array)
    cropped_array[mask] = img_array[mask]

    # Flip diagonal (kombinasi horizontal + vertical)
    flipped_array = np.zeros_like(cropped_array)
    flipped_array[mask] = cropped_array[::-1, ::-1][mask]

    # Simpan hasil
    Image.fromarray(cropped_array).save("cropped.png")
    Image.fromarray(flipped_array).save("crop_flip.png")
    print("✅ Hasil disimpan: cropped.png & crop_flip.png")

    # Tampilkan gambar
    plt.figure(figsize=(15,5))
    plt.subplot(1,3,1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.title("Crop Diagonal (Atas)")
    plt.imshow(cropped_array)
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.title("Crop + Flip Diagonal")
    plt.imshow(flipped_array)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
