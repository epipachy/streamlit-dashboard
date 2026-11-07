#print(type((13-4)/(12*12)))
#print(5//3) #ini bakal ngilangin angka di belakang koma
#print(5%3) #ini bakal print sisa bagi
#print(2**3) #ini pangkat
#print(3/3) #kenapa tiap pembagian hasilnya selalu float? mempermudah komputer aja 
#           biar ga ribet buat nentuin int/float jd disama ratain pake float
#xy = 3+4
#print(xy)
#pi = 22/7
#rad = 2.2
#area = pi*(rad**2)
#print(round(area, 3))
# https://pythontutor.com/visualize.html#mode=display buat visualisasi jalannya kode python


# LECTURE 2 
# STRING
#a = "love"
#b = "you"
#c = a + b # ni jd tanpa spasi
#c = a + " " + b #ni jd ada spasi
#silly = a * 3 # kalo mau pake operator *, bisanya kombinasi dr string sama number
#print(silly)
#b = ":"
#c = ")"
#print(2 * c)
#print(b+2*c)
#f = "a"
#g = " b"
#h = "3"
#s2 = (f+g) * int (h) # ini maksudnya 'a b' diulang 3 kali, hrs diubah int dulu h nya
#print(s2)

# SLICING TO GET ONE CHARACTER IN A STRING
# len () is a function used to retrieve the length of a string in the parentheses
#s = "abc"
#print(len(s)) # panjang stringnya brp character
#print(f"char = {len(s)}") 
#print(s[-3]) # ini buat print char berdasarkan index

# SLICING TO GET A SUBSTRING
#s = "abcdefgh"
# string[start:end] mulai dr index x, berhenti sebelum index y
#print(s[3:6])
# string[start:end:step] mulai dr index x, berhenti sebelum index y, lompat z langkah tiap kali
#print(s[3:6:2])
# ini sama aja kayak s[0:len(s):1]
#print(s[:])
# stringnya kebalik
#print(s[::-1])
# slicing mundur soalnya stepnya negatif
#print(s[4:1:-2])
#s = "ABC d3f ghi"
#print(s[3:len(s)-1])
#print(s[4:0:-1])
#print(s[6:3])

# IMMUTABLE STRINGS 
# maksudnya string itu gabisa diubah tp lu bisa bikin objek baru
#s = "car"
#s[0] = "b" #ni gagal
#s = "b" + s[1:len(s)] #ni baru bisa karena create objek baru, stop len(s) ni maksudnya stop sesuai berapa karakter yg ada
#print(s)

# PRINTING OUTPUT
#a = "the"
#b = 3
#c = "musketeers"
# print(a, b, c)
# print (a+b+c) # this is an error
#print (a + str(b) + c)  # kita ubah 3 jd string

# INPUT
# x = input("Type anything: ")
# print(5*x)
# num1 = input("Type a number: ") 
# print(5*num1) # hasilnya e.g. 3*5 = 33333 karena dibaca str
# num2 = int(input("Type a number: "))
# print(5*num2) # hasilnya e.g. 3*5 = 15 karena dibaca int

# verb = input("Type a verb: ")
# print(f"I can {verb} better than you!")
# print((verb+" ")*4 + verb)
# print(((verb + " ") * 5)[:-1]) # ni cara lain

