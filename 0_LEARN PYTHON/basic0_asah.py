#    TIPE DATA PRIMITIF    #

# IMPLEMENTASI DATA NUMBERS 
x = 6
print(type(x))
x = 6.0
print(type(x))
x = 1+2j
print(type(x))
# TIPE DATA NUMBERS IMMUTABLE (nilai tidak dapat berubah)
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))


# BOOLEAN
x = True
print(type(x))
x = False
print(type(x))


# STRING 
x = 'Dicoding'
print(type(x))
# MULTI-LINE (3 single/double quote)
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""
print(multi_line)
# SETIAP KARAKTER STRING PUNYA INDEKS
x = 'Dicoding'
print(x[0])
# GABISA NGUBAH STRING KARENA IMMUTABLE 
x = 'Dicoding'
x[0] = 'F'
# INDEXING DAN SLICING
x = 'Dicoding'
print(x[2:])
# TAMPILKAN STRING BERDASARKAN INPUT USER
name = "Perseus Evans"
print(f"Hello, nama saya {name}") # formatted string
print("Nama saya %s" % (name)) # %-formatting
print("Nama saya {}".format(name)) #str.format()



#    TIPE DATA COLLECTION   #

# LIST: kumpulan data terurut
x = [1, 2.2, 'Dicoding']
print(type(x))
# INDEXING
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0])
print(x[2])
print(x[-1])
print(x[-3])
# MUTABLE (bisa diubah valuenya)
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)
# SEQUENCE [start:stop:step]
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0:5:2])
print(x[1:])
print(x[:3])


# TUPLE: jenis dari list yg tidak dapat diubah valuenya
x = (1, "Dicoding", 1+3j)
print(type(x))
# INDEXING
x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])
# IMMUTABLE
x = (5, 'program', 1+3j)
x[1] = 'Dicoding'


# SET: kumpulan item unik tanpa urutan
x = {1,2,7,2,3,13,3}
print(x[0]) # error soalnya gapunya index
# TIDAK ADA DATA DUPLIKAT
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))
# SET=HIMPUNAN MTK, bisa pake operasi union sm intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
print("Union:", union)
intersection = set1.intersection(set2)
print("Intersection:", intersection)


# DICTIONARY: kumpulan pasangan key-value tidak berurut
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(type(x))
# GABISA INDEX soalnya ga urut
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(x[0]) # error 
# INSTEAD OF INDEXING, PANGGIL KEY NYA
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(x ['name'])
# TAMBAH DATA
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['Job'] = "Web Developer"
print(x)
# HAPUS DATA
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del x['isMarried']
print(x)
# UBAH DATA
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['name'] = "Dicoding"
print(x)



#    KONVERSI TIPE DATA   #
# INTEGER KE FLOAT
print(float(5))
# FLOAT KE INT
print(int(5.6))
print(int(-5.6))
# DARI-DAN-KE STRING
print(float("25"))
print(str(25.6))
# KUMPULAN DATA 
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
# KE DICTIONARY
print(dict([[1,2],[3,4]]))
print(dict([(3,25),(4,44)]))



#    TRANSFORMASI    #

# HURUF UPPER
kata = 'dicoding'
kata = kata.upper()
print(kata)
# HURUF LOWER
kata = 'DICODING'
kata = kata.lower()
print(kata)

# HAPUS WHITESPACE SBLH KANAN/AKHIR STRING 
print('Dicoding          '.rstrip() + ' Indonesia')
# HAPUS WHITESPACE SBLH KIRI/AWAL STRING
print('       Dicoding'.lstrip())
# HAPUS WHITESPACE AWAL DAN AKHIR STRING
print('    Dicoding   '.strip())
# HAPUS KARAKTER SELAIN WHITESPACE 
kata = 'CodeCodeDicodingCode'
print(kata.strip('Code'))


# TEMUKAN SUATU KATA AWAL STRING (nilai TRUE kalo ketemu)
print('Dicoding Indonesia'.startswith('Dicoding'))
# TEMUKAN SUATU KATA AKHIR STRING (nilai TRUE kalo ketemu)
print('Cindy Alya'.endswith('Alya'))


# GABUNGKAN STRING
print(' '.join(['Dicoding', 'Indonesia', '!'])) # '' sblm join itu delimiter
print(':'.join(['Anggur', 'Stroberi', 'Nanas'])) # delimiternya ganti jd :
# PISAHKAN STRING (kebalikan dr join)
print('Dicoding Indonesia !'.split()) # output ['Dicoding','Indonesia','!']
print('''Halo,
aku ikan,
aku suka sekali menyelam.'''.split('\n')) # ngilangin new line


# GANTI ELEMEN STRING
string = 'Ayo belajar Coding di Dicoding'
print(string.replace('Coding', 'Pemrograman')) # ubah coding jd pemrograman


# CEK STRING (true/false)
kata = 'DICODING'
print(kata.isupper()) # hasilnya bakal true 
kata = 'dicoding'
print(kata.islower()) # hasil true 
kata = 'dicoding'
print(kata.isalpha()) # true kalo semuanya alfabet
kata = 'dicoding123'
print(kata.isalnum()) # true kl ada angka, huruf, atau keduanga
print('123'.isdecimal()) # true kl hanya angka
print('    '.isspace()) # true hanya whitespace (spasi, tab, newline, dll)
print('Dicoding Indonesia'.istitle()) # true tiap huruf pertama kata kapital


# FORMATTING STRING
teks = 'Code'
tambah_number = teks.zfill(5) # buat nambah 0 di depan sebuah string.
print(tambah_number) # output 0Code
## panjang string 'Code' 4, jd program akan memastikan panjangnya 5 dgn nambah 0 di depan
## biasanya dipake buat menetapkan nomor nota/antrian
print('Dicoding'.rjust(20)) # biar teks rata kanan dgn nambahin whitespace
print('Dicoding'.rjust(20, '!')) # nambah ! sebanyak 12 + 8 dr char dicoding = 20
print('Dicoding'.ljust(20)) # rata kiri
print('Dicoding'.center(10, '-')) # whitespace kanan kiri default. bs nambahin char lain jg


# STRING LITERALS
# misal dlm bhs inggris i'm 
# stl = 'i'm'  kan salah dia, jd yg dianggap value cm sampe i doang, jd disarankan pakai ""
stl = "Jum'at"
# atau pakai escape character
stl = 'Jum\'at'
print("Halo!\nKapan terakhir kali kita ketemu?\nKita ketemu hari Jum'at") # outputnya bakal ke enter nanti (new line)


# RAW STRING
print(r'Dicoding\tIndonesia') # bikin semua karakter ikut kecetak



#    OPERASI PADA LIST, SET, DAN STRING    #
# len() utk menghitung panjang/banyaknya elemen
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9] # LIST
print(contoh_list)
print(len(contoh_list)) # output = 9
contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9]) # SET
print(contoh_list)
print(len(contoh_list)) # output = 5 karena listnya diubah ke set dulu (no duplikat)
contoh_string = "Belajar Python" # STRING
print(contoh_string)
print(len(contoh_string)) # output 14


# min() dan max()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
huruf = ["buah", "sayuran"]
print(min(angka)) # output 5
print(max(angka)) # outpput 96
print(min(huruf)) # output buah
print(max(huruf)) # output sayuran

# count()
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
huruf = ["ab", "abcde"]
print(genap.count(6)) # output 3
print(huruf.count("ab")) # output 1
string = "Belajar python di dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring)) # output 6


# In DAN Not In
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat) # true
print('tidak' in kalimat) # false
print('Dicoding' not in kalimat) # false
print('tidak' not in kalimat) # true


# MEMBERIKAN NILAI UNTUK MULTIPLE VARIABLE 
data = ['shirt', 'white', 'L']
apparel, color, size = data
print(data) # ['shirt', 'white', 'L']
print(apparel) # shirt
print(color) # white
print(size) # L


# Sort
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan) # ['helikopter', 'mobil', 'motor', 'pesawat']
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan) #  ['pesawat', 'motor', 'mobil', 'helikopter']
## gabisa campuran angka string
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()
print(kendaraan) # ['Pesawat', 'helikopter', 'mobil', 'motor'], ASCII jd kapital diduluin










