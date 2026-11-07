import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure

# Matriks citra dalam bentuk hexadecimal
hex_matrix = [
    ['A3','A4','AB','9A','90','A7','B1','A2'],
    ['7F','82','8B','8C','76','77','90','94'],
    ['64','70','6F','75','73','8D','B1','BC'],
    ['5F','67','5C','51','63','7E','AA','B5'],
    ['7B','5A','76','6B','58','60','7E','C6'],
    ['DD','7D','62','49','54','70','71','CD'],
    ['F2','A3','79','83','89','AC','6C','9A'],
    ['F2','9F','94','CF','CE','D4','A4','BB']
]

# Ubah ke array numpy dalam desimal (0-255)
image = np.array([[int(x, 16) for x in row] for row in hex_matrix], dtype=np.uint8)

# Tampilkan histogram sebelum ekualisasi
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.hist(image.flatten(), bins=256, color='gray')
plt.title("Histogram Sebelum Ekualisasi")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")

# Lakukan ekualisasi histogram
equalized = exposure.equalize_hist(image)
equalized = (equalized * 255).astype(np.uint8)

# Histogram sesudah ekualisasi
plt.subplot(1,2,2)
plt.hist(equalized.flatten(), bins=256, color='gray')
plt.title("Histogram Setelah Ekualisasi")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")

plt.tight_layout()
plt.show()

# ==============================
# Simpan hasil ke file .txt
# ==============================

with open("hasil_ekualisasi.txt", "w") as f:
    f.write("Hasil Ekualisasi Histogram\n")
    f.write("===========================\n\n")

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            before = image[y, x]
            after = equalized[y, x]
            line = f"f({x},{y}) = {before} -> {after}\n"
            f.write(line)

print("✅ File 'hasil_ekualisasi.txt' berhasil dibuat di folder kerja kamu!")
