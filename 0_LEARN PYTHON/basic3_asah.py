'''
def cari_luas_belah_ketupat (d1, d2):
    luas_belah_ketupat = 0.5 * d1 * d2
    return luas_belah_ketupat

print("Mencari luas belah ketupat, selamat mencoba!")
input_1 = int(input("Masukkan d1: "))
input_2 = int(input("Masukkan d2: "))
belah_ketupat = cari_luas_belah_ketupat(input_1, input_2)
print("Luas belah ketupat adalah: ", belah_ketupat)

def hitung_total(*args):
    total = sum(args)
    return total
print(hitung_total(2,3,4,5,6,7)) #ni bisa nambah angka sebanyak mungkin soalnya args tu tuple 


def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ": " + value + ", "
    return info

print(cetak_info(nama="Cindy", usia="20", pekerjaan="Mahasiswa"))

# fungsi tanpa def / fungsi one liner
# def func(args):
#     return ret_val
# bisa diganti
# func = lambda args: ret_val

cari_luas_persegi = lambda panjang, lebar: panjang*lebar
print(cari_luas_persegi(3,2))


def minimal (a,b):
    if a <= b:
        return a 
    else:
        return b

cari_minimal = minimal(300, 300)
print(cari_minimal)
'''

"""
TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
"""

class Animal:
     def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        
class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    def suara(self):
        return "meow!"

myCat = Cat("Neko", 3, "Persian")
print(myCat.deskripsi())
print(myCat.suara())
        
        