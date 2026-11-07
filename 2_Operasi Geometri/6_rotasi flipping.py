from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

# --------------------
#   GLOBAL LOG
# --------------------
log_lines = []
MAX_LOG = 4000   # batasi agar file tidak terlalu besar


# --------------------
#   BILINEAR INTERPOLATION
# --------------------
def bilinear_interpolation(img, x, y):
    h, w, c = img.shape

    if x < 0 or y < 0 or x >= w - 1 or y >= h - 1:
        return np.array([0, 0, 0], dtype=np.uint8)

    x0, y0 = int(x), int(y)
    x1, y1 = x0 + 1, y0 + 1

    dx, dy = x - x0, y - y0

    top_left     = img[y0, x0]
    top_right    = img[y0, x1]
    bottom_left  = img[y1, x0]
    bottom_right = img[y1, x1]

    top    = (1 - dx) * top_left + dx * top_right
    bottom = (1 - dx) * bottom_left + dx * bottom_right

    pixel = (1 - dy) * top + dy * bottom
    return pixel.astype(np.uint8)


# --------------------
#   ROTASI MANUAL BEBAS
# --------------------
def rotate_free(img_array, angle_deg):
    angle = math.radians(angle_deg)

    h, w, c = img_array.shape # ambil tinggi, lebar, sama channel gambar (rgb)

    # Hitung ukuran canvas baru agar tidak terpotong
    new_w = int(abs(w * math.cos(angle)) + abs(h * math.sin(angle)))
    new_h = int(abs(h * math.cos(angle)) + abs(w * math.sin(angle)))

    rotated = np.zeros((new_h, new_w, c), dtype=np.uint8)

    # Titik tengah lama & baru
    cx, cy = w / 2, h / 2
    ncx, ncy = new_w / 2, new_h / 2

    for y_new in range(new_h):
        for x_new in range(new_w):

            # Transform balik
            x_old = (x_new - ncx) * math.cos(angle) + (y_new - ncy) * math.sin(angle) + cx
            y_old = -(x_new - ncx) * math.sin(angle) + (y_new - ncy) * math.cos(angle) + cy

            # LOG ROTATE
            if len(log_lines) < MAX_LOG:
                log_lines.append(
                    f"x_old={int(x_old)}, y_old={int(y_old)} → x_new={x_new}, y_new={y_new}"
                )

            rotated[y_new, x_new] = bilinear_interpolation(img_array, x_old, y_old)

    return rotated


# --------------------
#   FLIPPING MANUAL
# --------------------
def flip_manual(img_array, mode):
    h, w, c = img_array.shape
    flipped = np.zeros_like(img_array)

    for y in range(h):
        for x in range(w):
            if mode == "1":      # Horizontal
                x_new = w - 1 - x
                y_new = y
            elif mode == "2":    # Vertikal
                x_new = x
                y_new = h - 1 - y
            elif mode == "3":    # Kombinasi
                x_new = w - 1 - x
                y_new = h - 1 - y
            else:
                raise ValueError("Mode flipping tidak valid.")

            # LOG FLIP (format sesuai contohmu)
            if len(log_lines) < MAX_LOG:
                log_lines.append(
                    f"f({x},{y}) → f'({x_new},{y_new}) "
                    f"dengan x' = {w}-1-{x} = {x_new}, y' = {y_new}"
                )

            flipped[y_new, x_new] = img_array[y, x]

    return flipped


# --------------------
#          MAIN
# --------------------
def main():
    path = input("Masukkan nama file gambar: ")
    img = Image.open(path).convert("RGB")
    arr = np.array(img)

    # ROTASI BEBAS
    angle = float(input("\nMasukkan sudut rotasi (boleh desimal, bebas): "))

    rotated = rotate_free(arr, angle)

    # FLIP SETELAH ROTASI
    print("\nPilih flipping:")
    print("1. Horizontal")
    print("2. Vertikal")
    print("3. Kombinasi")
    pil_flip = input("Masukkan pilihan (1/2/3): ")

    flipped = flip_manual(rotated, pil_flip)

    # SIMPAN TXT
    with open("hasil_koordinat.txt", "w", encoding="utf-8") as f:
        for line in log_lines:
            f.write(line + "\n")

    print("\n✔ hasil_koordinat.txt berhasil dibuat!")

    # SHOW GAMBAR
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 3, 1)
    plt.title("Asli")
    plt.imshow(arr)
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title(f"Rotasi {angle}°")
    plt.imshow(rotated)
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("Rotasi → Flip")
    plt.imshow(flipped)
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
