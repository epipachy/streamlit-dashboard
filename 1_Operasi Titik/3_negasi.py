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
    img_array = np.array(img, dtype=np.int16)
    Kmax = 255

    # Rumus: Ko = Kmax - Ki
    img_neg_array = np.clip(Kmax - img_array, 0, 255).astype(np.uint8)

    # 3️⃣ Simpan semua nilai f(x,y) ke file .txt
    txt_name = "hasil_negasi.txt"
    with open(txt_name, "w") as f:
        h, w, _ = img_array.shape
        f.write(f"Gambar: {image_path}\nUkuran: {h} x {w}\nOperasi: Negasi\n\n")
        for y in range(h):
            for x in range(w):
                for ch, ch_name in enumerate(["R","G","B"]):
                    Ki = img_array[y, x, ch]
                    Ko = img_neg_array[y, x, ch]
                    rumus = f"{Kmax} - {Ki}"
                    f.write(f"f({y},{x})[{ch_name}] = {rumus} = {Ko}\n")

    print(f"\n✅ Semua nilai f(x,y) sudah disimpan di file: {txt_name}")

    # 4️⃣ Konversi hasil kembali ke gambar
    img_neg = Image.fromarray(img_neg_array)

    # 5️⃣ Tampilkan gambar asli & hasil negasi
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Gambar Asli")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.title("Hasil Negasi")
    plt.imshow(img_neg)
    plt.axis("off")

    plt.show()

    # 6️⃣ Histogram per channel (RGB)
    colors = ('red', 'green', 'blue')
    channel_labels = ('R', 'G', 'B')

    plt.figure(figsize=(12,6))

    for i, color in enumerate(colors):
        plt.subplot(2,3,i+1)
        plt.title(f"Histogram {channel_labels[i]} Asli")
        plt.hist(img_array[:,:,i].flatten(), bins=256, range=(0,256), color=color, alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")

        plt.subplot(2,3,i+4)
        plt.title(f"Histogram {channel_labels[i]} Negasi")
        plt.hist(img_neg_array[:,:,i].flatten(), bins=256, range=(0,256), color=color, alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()