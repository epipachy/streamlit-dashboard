# This is my first python program
# print("Aku suka mie ayam!")
# print("It's really good!")

# VARIABLE = A container for value (string, integer, float, boolean)
#          = A variable behaves as if it was the value it contains

#String
#first_name = "Cindy"
#food = "mie ayam"
#email = "ciya@gmail"
#print(f"Hello aku {first_name}")
#print(f"Aku suka {food}")
#print(f"Emailku adalah: {email}")

#Integer
#age = 20
#quantity = 3
#num_of_students = 30
#print(f"Aku berumur {age} tahun")
#print(f"Aku beli buku {quantity} buah")
#print (f"Murid di kelas ada {num_of_students} siswa")

#Float
#price = 10.88
#gpa = 4.0
#distance = 5.5 
#print(f"harganya adalah ${price}")
#print(f"gpaku adalah: {gpa}")
#print(f"aku berlari sejauh {distance} km")

#Boolean
#is_student = True #first letter is capital
#for_sale = False
#is_online = True
#print(f"Are you a student?: {is_student}")

#if is_online:
    #print("You are online")
#else:
    #print("You are offline")





#TYPECASTING = the process of converting a variable from one data type to another 
#               str(). int(), float(), bool(). Useful buat ngetrack user input

#name = "Ciya"
#age = 20
#gpa = 3.8
#is_student = True

#print (type(gpa))

#gpa = int(gpa)
#print(gpa) => hasilnya nanti jadi 3 doang karena perubahan dr float ke int

#age = float(age)
#print(age) => nanti hasilnya jadi jadi 20.0 soalnya dia diubah dari int ke float

#age = str(age)
#print(type(age)) => ni jadi bukti kalo age nya berubah ke str bukan int lg

#name = bool(name)
#print(name) => apapun yg di isi di name akan keprint True, akan jd False kalo
#               ngga diisi apa2. Ini biasanya buat ngecek apakah suatu kolom diisi apa ngga





#INPUT = A function that promptr the user to enter data 
#       Returns the entered data as a string

#name = input("What is your name?: ")
#age = int (input("How old are you?: ")) #atau bisa juga pake cara ini, bakal sama ky line 80

#age = int(age)
#age = age + 1 #kalo mau ada ky gini hrs ganti ke int/float dulu, pake fungsi typecasting

#print(f"Hello {name}!")
#print("HAPYY BIRTHDAY!") #ga pake f string soalnya ga mau make variables
#print(f"You are {age} years old!")



#EXERCISES 1 Rectangle Area Calc

#length = float(input("Enter the length: "))
#width = float(input("Enter the width: "))
#area = length * width 

#print(f"The area is: {area} cm^2")

#EXERCISE 2 Shopping Cart Program

#item = input("What item would you like to buy?: ")
#price = float(input ("What is the price?: "))
#quantity = int(input("How many would you like?: "))
#otal = price * quantity

#print(f"You have bought {quantity} x {item}/s")
#print(f"Your total is: Rp. {total}")

# MADLIBS GAME
# word game where you create a story
# by filling in blanks with random words

#adjective1 = input("Enter and adjective (description): ")
#noun1 = input("Enter a noun (person, place, thing): ")
#adjective2 = input("Enter and adjective (description): ")
#verb1 = input("Enter a verb ending with -ing: ")
#adjective3 = input("Enter and adjective (description): ")

#print(f"Today i went to a {adjective1} zoo.")
#print(f"In an exhibit, i saw a {noun1}.")
#print (f"{noun1} was {adjective2} and {verb1}.")
#print (f"I was {adjective3}!")

#friends = 10
#friends = friends + 1
#friends += 1 #ini sama aja artinya kayak line 123, berlaku buat minus, kali, bagi jg
#friends = friends ** 2 #ini pangkat
#friends **= 2
#remainder = friends % 3 #ngitung sisa, jd kalo 10%3 hasilnya sisa 1

#print(remainder)


# x = 3.98
# y = -4
# z = 5

# result = round(x) # dibulatkan, misal 3.14 jadi 3. 3.98 jd 4.
# result = abs(y) # ini ngitung jarak absolute dari 0. misal -2 jarak abs nya 2.
# result = pow(4, 3) # artinya 4 pangkat 3. 
# result = max(x, y, z)
# result = min(x, y, z)
# print(result)

# import math

# x = 9.9
# print(math.pi)
# print(math.e) 
# result = math.sqrt(x) # akar
# result = math.ceil(x) # selalu ngebultin angka desimal ke atas
# result = math.floor(x) # selalu ngebuletin angka desimal ke bawah
# print(result) 

# EXERCISE 3
# import math
# radius = float(input("Enter the radius of a circle: ")) 
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)}") # artinya dibuletin belakang koma cuma ada 2 digit

#EXERCISE 4
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius, 2) # radius pangkat 2
# print(f"The circle area is: {round(area, 2)}")

# EXERCISE 5

#a = float(input("Enter side A: "))
#b = float(input("Enter side B: "))

#c = math.sqrt(pow(a, 2) + pow(b, 2))

#print(f"Side C = {round(c, 2)}")


# if = Do some code only IF some condition is True 
#       Else do something else

# age = int(input("Enter your age: "))

# if age >= 100:              #urutan eksekusi kondisi tu penting
#    print("You are too old to sign up!")
# elif age >= 18:
#    print("You are now signed up!")
# elif age < 0:
#    print("You havent been born yet!")
# else: 
#    print("You must be 18+ to signed up!")

#response = input("Would you like food? (Y/N): ")
#if response == "Y": 
#    print("Have some food!")
#else:
#    print("You have no food!")
    

#name = input("Enter your name: ")
#if name == "":
#    print("You have not entered your name!")
#else:
#    print(f"Hello {name}!")

#for_sale = True # ini bisa diganti false, buat menentukan hasil execute
#if for_sale:
#    print("This item is for sale")
#else:
#    print("This item is not for sale")
    

# EXERCISE 6 "PYTHON CALCULATOR"

#operator = input("Enter an operator (+ - * /): ")
#num1 = float(input("Enter the 1st number: "))
#num2 = float(input("Enter the 2nd number: "))

#if operator == "+":
#    result = num1 + num2
#    print(round(result, 2))
#elif operator == "-":
#    result = num1 - num2
#    print(round(result, 2))
#elif operator == "*":
#    result = num1 * num2
#    print(round(result, 2))
#elif operator == "/":
#    result = num1 / num2
#    print(round(result, 2))
#else:
#    print(f"{operator} is not a valid operator!")
    
# Python weight converter

#weight = float(input("Enter your weight: "))
#unit = input("Kilograms or Pounds? (K or L): ")

#if unit == "K":
#    weight = weight * 2.205
#    unit = "Lbs."
#    print(f"Your weight is: {round(weight, 1)} {unit}")
#elif unit == "L":
#    weight = weight / 2.205
#    unit = "Kgs."
#    print(f"Your weight is: {round(weight, 1)} {unit}")
#else:
#    print(f"{unit} was not valid.")

# temperature convertion program
#unit = input("Is this temperature in Celsius or Farenheit (C/F): ")
#temp = float(input("Enter the temperature: "))

#if unit == "C":
#    temp = round((9 * temp) / 5 + 32, 1)
#    print(f"The temperature in Farenheit is: {temp} derajat F")
#elif unit == "F":
 #   temp = round((temp - 32) * 5 / 9, 1)
  #  print(f"The temperature in Celsius is: {temp} derajat C")
#else:
 #   print(f"There is no {unit} in the measurement")      

firstName = str(input("Masukkan nama depan Anda: "))
lastName = str(input("Masukkan nama belakang Anda: "))
age = int(input("Masukkan umur Anda (cth: 20): "))
isMarried = bool(input("Apakah Anda sudah menikah? (True/False): ")) == "True"

print (f"Halo, nama aku {firstName} {lastName}!")
print(f"Aku berumur {age} tahun.")

if isMarried :
    print(f"Dan aku sudah menikah.")
else : 
    print(f"Dan aku belum menikah. ")








