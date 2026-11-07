'''
evenNumber = [n for n in range(501)]
print(evenNumber)

evenNumber = []
for n in range(501):  # range dipake buat sumber angka soalnya yg dilist maish kosong
  if n > 500:
    break
  else: 
    if n % 2 == 0:
        evenNumber.append(n)
print(evenNumber)
'''
'''
nama = ["Alya","Budi","Caca","Doni","Eka"]
for n in nama:
    print(n)

angka = [12,7,20,15,8,3,10]
for n in angka:
    if n % 2 == 0:
        print(n)

# program 0 - 20 tp 1 ganjil 2 genap gt 
for n in range (21):
    if n % 2 == 0: 
        print(n, "genap")
    elif n % 2 != 0:
        print(n, "ganjil")
        
# 0-100 tp pas 25 berhenti, 25 g kecetak
for n in range (101):
    if n >= 25:
        break
    else:
        print(n)

# list lulus >= 70
nilai = [80, 65, 90, 45, 70, 55, 95]
lulus = []
for n in nilai:
    if n >= 70:
        lulus.append(n)
print(lulus)

# 3 meja tiap meja 4 kursi
for i in range (1,4):
    for j in range (1,5):
        print("Meja", i,"- Kursi", j)

# ada kelas 1 2 3, kalo >= 70 cetak lulu kl < 70 cetak tidak lulus
nilai = [
    [80, 65, 90],
    [55, 70, 60],
    [95, 88, 72]
]

for i in range (1,4):
    for j in nilai[i-1]:
        if j >= 70:
            print("Kelas", i, "-", j, "- Lulus")
        else:
            print("Kelas", i, "-", j, "- Tidak Lulus")


umur = 16
print("Dewasa") if umur >=18 else print("Anak-Anak")

angka = []
for n in range(1,31):
    if n % 3 == 0 and n % 5 ==0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
        
        
angka = int(input("Masukkan angka: "))
while angka != 0:
    print(angka * 2)
    angka = int(input("Masukkan angka: "))
print("Program selesai")

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))
'''
for n in range(1,51):
    if n % 7 == 0:
        continue
    print(n)

suhu = [30, 15, 22, 5, 40, 18]

belanja = [
    ["Baju", 150000],
    ["Sepatu", 300000],
    ["Topi", 50000],
    ["Tas", 250000]
]

for i in range (1,5):
    for j in belanja[i-1][i-1]:
        if j > 100000:
            print("Mahal")
        else:
            print("Murah")
    







