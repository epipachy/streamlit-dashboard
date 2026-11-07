# autosmart_crop_flip.py
from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt

def remove_border(img, tol=10):
    """Hapus border/kanvas yang seragam (mis. putih/abu muda) menggunakan ImageChops."""
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    bg = Image.new("RGBA", img.size, img.getpixel((0,0)))
    diff = ImageChops.difference(img, bg)
    # sedikit tambah toleransi agar noise kecil tidak dianggap isi
    diff = ImageChops.add(diff, diff, 2.0, -tol)
    bbox = diff.getbbox()
    if bbox:
        return img.crop(bbox)
    return img

def find_water_line(arr, blue_thresh=120, min_frac=0.15):
    """
    Cari baris pertama (dari atas) yang kemungkinan besar adalah awal 'air' (banyak pixel biru).
    - arr: numpy array HxWx3 (RGB)
    - blue_thresh: minimal B value untuk pixel dianggap 'biru'
    - min_frac: minimal fraksi kolom dalam baris yang harus biru agar baris dianggap 'air'
    """
    H, W, _ = arr.shape
    for y in range(H):
        row = arr[y,:,:]
        blue_mask = (row[:,2] > blue_thresh) & (row[:,0] < 150) & (row[:,1] < 150)
        if blue_mask.sum() / W >= min_frac:
            return y
    return None

def bbox_from_mask(mask):
    """Dari boolean mask (HxW) kembalikan (left, top, right, bottom) bounding box."""
    ys, xs = np.where(mask)
    if ys.size == 0:
        return None
    top, bottom = ys.min(), ys.max()
    left, right = xs.min(), xs.max()
    return left, top, right+1, bottom+1  # +1 supaya eksklusif kanan/bawah seperti PIL

def auto_process(filename, show=True):
    # 1) load + convert to RGBA (untuk aman)
    img0 = Image.open(filename).convert("RGBA")

    # 2) optional: ubah transparan -> putih supaya deteksi warna tidak terganggu
    arr0 = np.array(img0)
    if arr0.shape[2] == 4:
        alpha = arr0[...,3]
        arr0[alpha == 0] = [255,255,255,255]
        img = Image.fromarray(arr0, "RGBA").convert("RGB")
    else:
        img = img0.convert("RGB")

    # 3) remove uniform border (frame) agar crop lebih rapat
    img = remove_border(img.convert("RGBA"), tol=10).convert("RGB")
    W, H = img.size
    arr = np.array(img)

    # 4) cari waterline (baris pertama dengan cukup banyak piksel biru)
    water_y = find_water_line(arr, blue_thresh=120, min_frac=0.12)
    if water_y is None:
        # fallback: pakai setengah bawah
        water_y = H // 2

    # 5) crop top area (area gedung) dan bottom area (air)
    top_region = img.crop((0, 0, W, water_y))
    bottom_region = img.crop((0, water_y, W, H))

    # 6) Untuk top_region: buat mask non-background untuk cari bounding box isi (hindari L-shape besar)
    top_arr = np.array(top_region)
    # anggap background terang (putih/abu) sebagai background; non-bg = ada warna lebih gelap
    nonbg_mask = np.any(top_arr < 245, axis=2)  # True untuk pixel bukan putih cerah
    bbox_top = bbox_from_mask(nonbg_mask)
    if bbox_top:
        left_t, top_t, right_t, bottom_t = bbox_top
        gedung = top_region.crop((left_t, top_t, right_t, bottom_t))
    else:
        # jika deteksi gagal, fallback ambil seluruh top_region
        gedung = top_region

    # 7) Untuk bottom_region: cari bounding box area biru (ketat)
    bottom_arr = np.array(bottom_region)
    blue_mask = (bottom_arr[:,:,2] > 110) & (bottom_arr[:,:,0] < 150) & (bottom_arr[:,:,1] < 150)
    bbox_bottom = bbox_from_mask(blue_mask)
    if bbox_bottom:
        left_b, top_b, right_b, bottom_b = bbox_bottom
        # bbox_bottom adalah relatif ke bottom_region; ubah ke koordinat global bottom
        air = bottom_region.crop((left_b, top_b, right_b, bottom_b))
    else:
        # fallback: gunakan seluruh bottom_region
        air = bottom_region

    # 8) flip gedung (vertikal seperti tugasmu)
    gedung_flip = gedung.transpose(Image.FLIP_TOP_BOTTOM)

    # 9) Buat canvas dinamis (lebar = max lebar, tinggi = air.height + gedung_flip.height)
    aW, aH = air.size
    gW, gH = gedung_flip.size
    canvas_W = max(aW, gW)
    canvas_H = aH + gH
    output = Image.new("RGB", (canvas_W, canvas_H), (255,255,255))

    # 10) tempatkan air (kita tempatkan di x=0 agar definisi kanan bawah konsisten)
    output.paste(air, (0, 0))

    # 11) paste gedung_flip ke kanan–bawah relatif ke canvas
    paste_x = canvas_W - gW
    paste_y = canvas_H - gH
    output.paste(gedung_flip, (paste_x, paste_y))

    # 12) tampilkan hasil perbandingan jika diminta
    if show:
        plt.figure(figsize=(12,6))
        plt.subplot(1,3,1)
        plt.title("Original (trimmed)")
        plt.imshow(img)
        plt.axis("off")

        plt.subplot(1,3,2)
        plt.title("Detected parts\n(top=gedung, bottom=air)")
        # overlay bounding boxes for debug
        debug = img.copy()
        draw = Image.fromarray(np.array(debug))
        ax = plt.gca()
        plt.imshow(debug)
        # draw rectangles manually with matplotlib so they appear above image
        # gedung bbox in top_region coordinates -> convert to original:
        if bbox_top:
            lx, ty, rx, by = bbox_top
            # draw rectangle
            rect = plt.Rectangle((lx, ty), rx-lx, by-ty, edgecolor='r', facecolor='none', linewidth=2)
            ax.add_patch(rect)
        if bbox_bottom:
            lx, ty, rx, by = bbox_bottom
            # bottom_region was at y=water_y, so shift y by water_y
            rect2 = plt.Rectangle((lx, water_y+ty), rx-lx, by-ty, edgecolor='b', facecolor='none', linewidth=2)
            ax.add_patch(rect2)
        plt.axis("off")

        plt.subplot(1,3,3)
        plt.title("Transformed (Right-Bottom)")
        plt.imshow(output)
        plt.axis("off")

        plt.show()

    return output

if __name__ == "__main__":
    fname = input("Masukkan nama file gambar: ")
    out = auto_process(fname, show=True)
    out.save("hasil_auto.png")
    print("Selesai. Disimpan sebagai hasil_auto.png")