#     JENIS - JENIS EKSPRESI   #
# 1. OPERASI BINER = memiliki dua operan. operatornya +, -, *, /, **(perpangkatan), <, <=, >, >=, %, ==, !=
# misal: (x+y), (x-y)
# 2. OPERASI UNER = memiliki bentuk dasar 1 operan. 
# misal: increment (x+=1), decrement(x-=1), dan negasi(not x)

# EKSPRESI UNER
a = True
a = not a
print(a) # output False
b = 6
b -= 1
print(b) # output 5
c = 6
c += 1
print(c) # output 7
d = 10
print(-d) # output -10


# EKSPRESI MENURUT TIPE DATA YG DIHASILKAN
# 1. Eks. aritmetika: <numerik> <operator> <numerik> = <num>. Cont. 2 + 2 = 4
# 2. Eks. relasional: <numerik> <operator> <numerik> = <bool>. Cont. 3 < 10 = True
# 3. Eks. logika: <bool> <operator> <bool> = <bool>. Cont. True or False = True
print(2+2) # output 4
print(3<10) # output True
print(True or False) # output True


# JENIS - JENIS OPERATOR
# 1. Operator Aritmatika
x = 11
y = 5
print(x + y) # 16
print(x - y) # 6
print(x * y) # 55
print(x // y) # 2 PEMBAGIAN BULAT. 
print(x / y) # 2.2
print(x % y) # 1
print(x ** y) # 161051
# 2. Operator Relasional
x = 5
y = 10
print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False
print(x <= y) # True
# 2.1 Operator Relasional String
# 2.1.1 Sama dengan (==) Menghasilkan True, jika kedua string memiliki nilai yang identik/sama persis.
# contoh x == y, menghasilkan False.
# 2.1.2 Tidak Sama dengan (!=) Menghasilkan True, jika kedua string memiliki nilai yang tidak sama.
# contoh x != y, menghasilkan True.
# 2.1.3 Lebih Besar dari (>) Menghasilkan True, jika huruf pertama pada string pertama memiliki nilai unicode dengan urutan yang lebih tinggi dibandingkan huruf pertama pada string kedua. 
# contoh x > y, menghasilkan False.
# 2.1.4 Kurang dari (<) Menghasilkan True, jika huruf pertama pada string pertama memiliki nilai unicode dengan urutan yang lebih rendah dibandingkan huruf pertama pada string kedua.
# contoh x < y, menghasilkan True.
# 2.1.5 Lebih Besar dari Sama dengan (>=) Menghasilkan True, jika huruf pertama pada string pertama memiliki nilai unicode dengan urutan yang lebih tinggi atau sama dibandingkan huruf pertama pada string kedua.
# contoh x >= y, menghasilkan False.
# 2.1.6 Kurang dari Sama dengan (<=) Menghasilkan True, jika huruf pertama pada string pertama memiliki nilai unicode dengan urutan yang lebih rendah atau sama dibandingkan huruf pertama pada string kedua.
# contoh x <= y, menghasilkan True.
## Catatan: Nilai unicode adalah standar internasional yang menetapkan kode numerik untuk setiap karakter dari hampir semua sistem tulisan dan simbol-simbol yang digunakan oleh manusia.
x = "Dicoding"
y = "Indonesia"
print(x == y) # false
print(x != y) # true
print(x > y) # false
print(x < y) # true
print(x >= y) # false
print(x <= y) # true
# 3. Operator Logika (asumsikan p true q false)
# "AND" atau "&" Logika yang hanya menghasilkan True jika kedua operan bernilai True.
# contoh: p and q = False, p & q = False
# "OR" atau "|" Logika yang menghasilkan True jika salah satu dari kedua operan bernilai True.
# contoh: p or q = True, p | q = True
# NOT Logika yang bertujuan untuk membalikkan nilai logika dari operannya.
# contoh: not q = True
print(True and True) # true
print(True and False) # false
print(False and True) # false
print(False and False) # false 
print(True or True) # true
print(True or False) # true
print(False or True) # true 
print(False or False) # false
print(not True) # false
print(not False) # true
# 4. Operasi Assignment (asumsi x=11 y=5)
# +=    Menyederhanakan operasi x = x + y.
# contoh: x += y, menghasilkan nilai 16.
# -=    Menyederhanakan operasi x = x - y.
# contoh: x -= y, menghasilkan nilai 6.
# *=    Menyederhanakan operasi x = x * y.
#contoh: x *= y, menghasilkan nilai 55.
# /=    Menyederhanakan operasi x = x / y.
# x /= y, menghasilkan nilai 2.2.
# %=    Menyederhanakan operasi x = x % y.
# x %= y, menghasilkan nilai 1.
# +=
x = 11
x += 5
print(x) # 16
# -=
x = 11
x -= 5
print(x) # 6
# *=
x = 11
x *= 5
print(x) # 55
# /=
x = 11
x /= 5
print(x) # 2.2
#%=
x = 11
x%= 5
print(x) # 1