from PIL import Image

def main():
    # 1️⃣ Meminta input nama file citra
    image_path = input(" masukkan nama gambar: ")

    try:
        # 2️⃣ Buka citra
        img = Image.open(image_path)
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan citra ada di folder yang sama dengan script.")
        return

    # 3️⃣ Resolusi citra
    width, height = img.size
    print(f"\nResolusi citra: {width} x {height}")

    # 4️⃣ Kedalaman warna
    mode = img.mode
    if mode == '1':
        depth = "1-bit (black & white)"
    elif mode == 'L':
        depth = "8-bit grayscale"
    elif mode == 'RGB':
        depth = "24-bit RGB"
    elif mode == 'RGBA':
        depth = "32-bit RGB + Alpha"
    else:
        depth = mode
    print(f"Kedalaman warna: {depth}")

    # 5️⃣ Nilai f(x,y)
    print("\nNilai f(x,y) (contoh 5x5 piksel pertama):")
    for y in range(min(5, height)):
        for x in range(min(5, width)):
            print(img.getpixel((x, y)), end=' ')
        print()

    # 6️⃣ Simpan semua nilai piksel ke file teks
    output_file = "nilai_pixel.txt"
    with open(output_file, "w") as f:
        for y in range(height):
            for x in range(width):
                f.write(str(img.getpixel((x, y))) + " ")
            f.write("\n")
    print(f"\nSemua nilai piksel telah disimpan di '{output_file}'")

if __name__ == "__main__":
    main()
