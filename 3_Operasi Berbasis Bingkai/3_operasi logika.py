from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== Operasi Logika Citra ===")

    # 1️⃣ Input dua file gambar
    fileA = input("Masukkan nama file citra A: ")
    fileB = input("Masukkan nama file citra B: ")

    try:
        A = Image.open(fileA).convert("L")  # ubah ke grayscale
        B = Image.open(fileB).convert("L")
    except FileNotFoundError:
        print("❌ File tidak ditemukan. Pastikan nama dan path benar.")
        return

    # Samakan ukuran B dengan A
    B = B.resize(A.size)

    # 2️⃣ Ubah ke array numpy
    A_arr = np.array(A, dtype=np.uint8)
    B_arr = np.array(B, dtype=np.uint8)

    # 3️⃣ Pilih operasi logika
    print("\nPilih operasi logika:")
    print("1. AND")
    print("2. OR")
    print("3. XOR")
    print("4. SUB")
    print("5. NOT (hanya citra A)")
    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "1":
        hasil = np.bitwise_and(A_arr, B_arr)
        operasi = "AND"
    elif pilihan == "2":
        hasil = np.bitwise_or(A_arr, B_arr)
        operasi = "OR"
    elif pilihan == "3":
        hasil = np.bitwise_xor(A_arr, B_arr)
        operasi = "XOR"
    elif pilihan == "4":
        hasil = np.maximum(A_arr - B_arr, 0)
        operasi = "SUB"
    elif pilihan == "5":
        hasil = np.bitwise_not(A_arr)
        operasi = "NOT"
    else:
        print("❌ Pilihan tidak valid.")
        return

    # 4️⃣ Simpan hasil perhitungan ke .txt
    txt_name = f"hasil_{operasi}.txt"
    with open(txt_name, "w") as f:
        h, w = A_arr.shape
        f.write(f"Citra A: {fileA}\n")
        if pilihan != "5":
            f.write(f"Citra B: {fileB}\n")
        f.write(f"Ukuran: {h} x {w}\n")
        f.write(f"Operasi: {operasi}\n\n")

        for y in range(h):
            for x in range(w):
                if operasi == "NOT":
                    f.write(f"f({x},{y}) = ~{A_arr[y,x]} -> {hasil[y,x]}\n")
                elif operasi == "SUB":
                    diff = A_arr[y,x] - B_arr[y,x]
                    if diff < 0:
                        f.write(f"f({x},{y}) = {A_arr[y,x]} - {B_arr[y,x]} = {diff} -> 0\n")
                    else:
                        f.write(f"f({x},{y}) = {A_arr[y,x]} - {B_arr[y,x]} -> {hasil[y,x]}\n")
                else:
                    symbol = {"AND":"&", "OR":"|", "XOR":"^"}[operasi]
                    f.write(f"f({x},{y}) = {A_arr[y,x]} {symbol} {B_arr[y,x]} -> {hasil[y,x]}\n")

    print(f"\n✅ Semua hasil perhitungan tersimpan di file: {txt_name}")

    # 5️⃣ Simpan hasil gambar
    out_name = f"hasil_{operasi}.png"
    Image.fromarray(hasil.astype(np.uint8)).save(out_name)
    print(f"✅ Gambar hasil disimpan sebagai: {out_name}")

    # 6️⃣ Tampilkan gambar hasil
    plt.figure(figsize=(10, 4))
    if pilihan == "5":  # NOT
        plt.subplot(1, 2, 1)
        plt.title("Citra A")
        plt.imshow(A_arr, cmap="gray")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.title("NOT A")
        plt.imshow(hasil, cmap="gray")
        plt.axis("off")
    else:
        plt.subplot(1, 3, 1)
        plt.title("Citra A")
        plt.imshow(A_arr, cmap="gray")
        plt.axis("off")

        plt.subplot(1, 3, 2)
        plt.title("Citra B")
        plt.imshow(B_arr, cmap="gray")
        plt.axis("off")

        plt.subplot(1, 3, 3)
        plt.title(f"Hasil {operasi}")
        plt.imshow(hasil, cmap="gray")
        plt.axis("off")

    plt.tight_layout()
    plt.show()

    # 7️⃣ Tampilkan histogram dengan skala Y yang sama
    plt.figure(figsize=(12, 4))

    histA, _ = np.histogram(A_arr.flatten(), bins=256, range=(0, 256))
    histB, _ = np.histogram(B_arr.flatten(), bins=256, range=(0, 256))
    histHasil, _ = np.histogram(hasil.flatten(), bins=256, range=(0, 256))

    # cari nilai maksimum biar semua punya skala sama
    y_max = max(histA.max(), histB.max(), histHasil.max())

    if pilihan == "5":  # NOT
        plt.subplot(1, 2, 1)
        plt.title("Histogram Citra A")
        plt.hist(A_arr.flatten(), bins=256, range=(0, 256), color="gray", alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")
        plt.ylim(0, y_max)

        plt.subplot(1, 2, 2)
        plt.title("Histogram Hasil NOT A")
        plt.hist(hasil.flatten(), bins=256, range=(0, 256), color="gray", alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")
        plt.ylim(0, y_max)
    else:
        plt.subplot(1, 3, 1)
        plt.title("Histogram Citra A")
        plt.hist(A_arr.flatten(), bins=256, range=(0, 256), color="gray", alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")
        plt.ylim(0, y_max)

        plt.subplot(1, 3, 2)
        plt.title("Histogram Citra B")
        plt.hist(B_arr.flatten(), bins=256, range=(0, 256), color="gray", alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")
        plt.ylim(0, y_max)

        plt.subplot(1, 3, 3)
        plt.title(f"Histogram Hasil {operasi}")
        plt.hist(hasil.flatten(), bins=256, range=(0, 256), color="gray", alpha=0.7)
        plt.xlabel("Intensitas Piksel")
        plt.ylabel("Frekuensi")
        plt.ylim(0, y_max)

    plt.tight_layout()
    plt.show()

# ✅ Entry point
if __name__ == "__main__":
    main()
