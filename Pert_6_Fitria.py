#kode 1
While True:
 Print(“loops tak hingga")
 
#kode 2 
 counter = 8
while counter > 2:
 print(counter) 
 counter -= 1
 
#kode 3 
 #membuat variabel angka ganjil dan angka genap
angka_genap = 0
angka_ganjil = 0
#membada angka pertama
angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))
while angka != 0: #cek apakah angka tidak sama dengan 0
 if angka % 2 == 1: #mengecek apakah sisa bagi angka dengan 2 adalah 1
 angka_ganjil += 1
 else:
 angka_genap += 1
 #membaca angka berikut
 angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))
#menampilkan total angka ganjil dan angka genap
print("Jumlah Angka Ganjil: ", angka_ganjil)
print("Jumlah Angka Ganjil: ", angka_genap)

#kode 4
secret_number = 88
while True:
 angka = int(input("Masukkan angka rahasia: "))
 
 if angka == secret_number:
 print("Selamat, Muggle! kamu bebas sekarang!")
 break
 else:
 print("hahaha! kamu nyangkut deh di Loop saya")
 
#kode 5 
 #perbandingan a,b,c,d
for a in range(10):
 print("Nilai a saat ini adalah", a)
for b in range(2,8):
 print("Nilai b saat ini adalah", b)
for c in range(2,8,3):
 print("Nilai c saat ini adalah", c)
 for d in range(1,1):
 print("Nilai d saat ini adalah", d)
for e in range(2,1):
 print("Nilai e saat ini adalah", e)
 
#kode 6 
 n = int(input("Masukkan pangkat: "))
hasil = 1
for i in range(n):
 hasil = hasil * 2
print("Hasil 2 pangkat", n, "adalah", hasil)

#kode 7
for i in range(1, 6):
 if i == 3:
 continue
 if i == 5:
 break
 print(i)

#kode 8 
 print("=== GAME TEBAK ANGKA PESULAP ===")
print("Pesulap telah menyimpan angka rahasia antara 1 - 20")
angka_rahasia = 15
while True:
 tebakan = int(input("Tebak angkanya: "))
 if tebakan == angka_rahasia:
 print("Hebat! Kamu berhasil menebak angka rahasia pesulap!")
 break
 elif tebakan > angka_rahasia:
 print("Angka terlalu besar!")
 else:
 print("Angka terlalu kecil!")
 
#kode 9 
 kata = input("Masukkan sebuah kata: ")
kata = kata.upper()
print("Huruf konsonan yang tersisa:")
for huruf in kata:
 if huruf == "A":
 continue
 elif huruf == "I":
 continue
 elif huruf == "U":
 continue
 elif huruf == "E":
 continue
 elif huruf == "O":
 continue
 else:
 print(huruf)

#kode 10 
 i = 1
while i <= 3:
 print("Perulangan ke-", i)
 i += 1
else:
 print("Perulangan selesai")

#kode 11 
 for i in range(3):
 print("Angka:", i)
else:
 print("Perulangan for selesai")

#kode 12 
 umur = 20
punya_ktp = True
if umur >= 17 and punya_ktp:
 print("Boleh memilih")
else:
 print("Tidak boleh memilih")
 
#kode 13 
 Logical
a = True
b = False
print(a and b)
print(a or b)
print(not a)
Bitwise operator 
x = 5
y = 3
print(x & y)
print(x | y)
print(x ^ y)

#kode 14
a = 8
print(a << 1) 
print(a >> 1)

#kode 15
x = 4
y = 1
a = x & y
b = x | y
c = ~x 
d = x ^ 5
e = x >> 2
f = x << 2
print(a,b,c,d,e,f)