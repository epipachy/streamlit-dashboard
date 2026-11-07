##      PERCABANGAN & TERNARY OPERATORS     ##

# 1. PERCABANGAN: "JIKA-MAKA" (if-else)
ketersediaan = "Daging Ayam"
if ketersediaan == "Daging Ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")
## output: Ibu membeli dan memasak ayam
## if merupakan statement python utk cek value variabel apakah memenuhi kondisi atau tidak
score = 100 # inisiasi nilai score
if score == 100: #akan diproses apabila value bernilai True
    print("Nilai Anda Sempurna!") #akan diproses apabila value bernilai True
## nilai kosong(zero) dan null adalah false
x = ""
if x:
    print("Ini True") # gaakan ada output/kosong karena diinisiasi dgn string kosong
## output: 
## nilai2 yg dianggap false sm python:
## none dan false; numerik 0, 0.0, 0j, Decimal(0), Fraction(0,1); "",(),[],{},set(),range(0)
## if statement juga bisa one-liner
score = 100
if score == 100: print("Nilai anda sempurna!")
## output: Nilai anda sempurna!
## else merupakan statement jalan keluar saat kondisi if statement bernilai false
tinggi_badan = 120 # inisiasi variabel
if tinggi_badan >= 160: # jika tinggi lebih dr 160 boleh naik
    print("Anda boleh menaiki roller caoster") # ga dieksekusi krn ga memenuhi (false)
else:
    print("Anda tidak diperbolehkan menaiki roller coaster") # dieksekusi krn if bernilai false
## output: Anda tidak diperbolehkan menaiki roller coaster
## elif merupakan kependekan dari else if dan alternatif untuk if bertingkat atau switch case. posisinya setelah if
nilai = 65
if nilai>=80:
    print("GACORR!! GG!! Selamat selimit km dapat A")
    print("ASEKKKK, pertahankan ia!")
elif nilai>=70:
    print("WOWWW alhamdulillah dpt B dik km")
    print("Kemren tp tingkatkan ia biar bs bikin jj caaaantik")
elif nilai>=60:
    print("Hmm.. km dpt C jir...")
    print("Ndakpapa dik blm ngulang koq enih, giat lg iyah,,") 
else:
    print("Waduh........ D hehe")
    print("Belajar lg yah synk,, cemunguy~~") 
## output : Hmm.. km dpt C jir... \n Ndakpapa dik blm ngulang koq enih, giat lagi iyah,,
## bisa juga nambahin 'and' atau 'or' dlm percabangan
nilai = 81
perilaku = "tidak baik"

if nilai>=80 and perilaku == "baik":
    print("Selamat selimit km dpt A, km jg good etitud")
elif nilai>=80 and perilaku != "tidak baik":
    print("Slamat km dpt A tp kelakuanmu ky kentut, ubah mindset km")
else:
    print("Jir udh nilai jlk, etitud minus, mw km ap dik..")
## output: Slamat km dpt A tp kelakuanmu ky kentut, ubah mindset km


# TERNARY OPERATORS
## merupakan conditional expression utk evaluasi kondisi dan mengembalikan nilai hasil evalnya
## asumsi versi one-liner dr if-else
lulus = True
print("Selamat") if lulus else print("perbaiki")
## output: selamat
## opsi lain bs melibatkan tuple
lulus = True
kelulusan = ("perbaiki, anda belum lulus", "selamat, anda lulus") [lulus]
print(kelulusan)
## output: selamat, anda lulus. soalnya kan pake 0,1. nah kan insiasinya true alias 1


##       PERULANGAN      ##

# For
## bersifat define iteration yg merupakan proses iterasi ketika jumlah pengulangan ditentukan secara eksplisit sebelumnya
## formatnya: for <var> in <iterable>:
##               <statement(s)>
## <iterable> segala object python yg dapat diiterasi (list, tuple, string)
## <var> variable yg mengambil elemen berikutnya dr <iterable> tiap kali iterasi berjalan
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)
## output: 1 \n 2 \n 3 dst..
## bisa pake fungsi range()
for i in range(10):
    print(i)
## output 0-9 karena range pakenya index
## sintaks umum dr range()
##      range(start,stop,step)
for i in range(1,10,2):
    print(i)
## output: 1,3,5,7,9


# While
## indefine iteration, proses iterasi akan berhenti ketika memenuhi kondisi tertentu
## formatnya: while kondisi:
##              # blok pernyataan yg akan diulang selama kondisi bernilai true
counter = 1
while counter <=5:
    print(counter)
    counter += 1 # increment.
## output: 1,2,3,4,5
## increment adl pola utk nambahin suatu variabel yg nilainya tetap
## hati hati akan infinite loop kalo ga dikasih increment/decrement


# For Bersarang
## perulangan dalam perulangan (nested loop)
## formatnya: for variabel_luar in iterabel_luar:
##              for variabel_dalam in iterabel_dalam:
##                  # blok pernyataan yg akan diulang
for i in range(1, 3): # outer loop
    for j in range(1, 3): # inner loop
        print(i,j)
## output: 1,1 \n 1,2 \n 2,1 \n 2,2



##      KONTROL PERULANGAN      ##
# Break
## adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya.
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1
"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
"""

# Continue
## pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. 
## Continue seolah mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok.
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
Huruf saat ini: d   # Perhatikan bahwa harusnya sebelum ini ada spasi, namun dilewati.
Huruf saat ini: i
Huruf saat ini: n
Huruf saat ini: g
"""

# Else setelah For
## untuk perulangan bersifat pencarian. 
## bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

"""
Output:
Angka tidak ditemukan.
"""
## break dalam if harus tidak terjadi untuk memicu else setelah for.


# Else setelah While
## blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah. 
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")


"""
Output:
Dicoding Indonesia
Dicoding Indonesia
Dicoding Indonesia
Blok else dieksekusi karena kondisi pada while salah (3<3 == False).
"""
## ini kalo pake break
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

"""
Output:
9
8
"""

# Pass
## pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

"""
Output:


"""
## biasanya dibutuhin placeholder utk nenujukin kalo gaada operasi yg perlu dolakukan


# List Comperhension
## membuat sebuah list baru berdasarkan list yang sudah ada.
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

"""
Output:
[1, 4, 9, 16]

"""

angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

"""
Output:
[1, 4, 9, 16]
"""

    

