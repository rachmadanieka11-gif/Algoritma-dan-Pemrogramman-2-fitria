#1
x = 0
y = 2
z = 0
print(x == y)
print(x == y)
print(x != y)
print(x < y)
print(y < x)
print(x > y)
print(x <= y)
print(x <= z)
print(x <= z)
print(x >= y)
print(x >= z)

#2
n = int(input("Masukkan nilai n: "))
print(n>100)
print(n<100)

#3
x = 12
if x == 12:
    print("x sama dengan 12")
    
#4    
x = 12
if x > 12:
    print("x lebih besar dari 12")
if x < 12:
    print("x lebih kecil dari 12")
if x == 12:
    print("x sama dengan 12")
    
#5
x = 12
if x > 14:
    print("x lebih kecil dari 14")
else:
    print("x lebih besar atau sama dengan 14")
    
#6
x = 12

if x == 12:
    print("x == 12")
elif x > 14:
    print("x > 14")

if x > 2:
    print("x > 2")
else:
    print("x lebih kecil dari 2")
    
#7
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if angka1 > angka2:
    angka_besar = angka1
else:
    angka_besar = angka2
print("angka yang besar adalah", angka_besar)

#8
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

if angka1 > angka2: 
    angka_besar = angka1
elif angka2 > angka3:
    angka_besar = angka2
elif angka1 < angka3:
    angka_besar = angka3
else:
    angka_besar = angka3      
print("angka yang besar adalah", angka_besar) 

#9
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

angka_besar = max (angka1, angka2, angka3)
print("angka paling besar adalah angka_besar")

#10
pendapatan_bulanan = float(input("Masukkan pendapatan bulanan: "))
pajak = 0
pendapatan_tahunan = pendapatan_bulanan*12

if pendapatan_bulanan <= 60000000:
    tarif = 0.05
elif pendapatan_tahunan <= 250000000:
    tarif = 0.15
elif pendapatan_tahunan <= 500000000:
    tarif = 0.25        
else:
    tarif = 0.30
pajak = pendapatan_tahunan  * tarif 
print("Tarif pajak anda: ", tarif *100, "%" )      
print("Pajak penghasilan yang harus dibayarkan", pajak, "rupiah")