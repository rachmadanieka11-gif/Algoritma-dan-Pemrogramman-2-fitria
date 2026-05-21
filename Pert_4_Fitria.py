#codingan 1
print("The Fate of Ophelia...")
of = input()
print("Keep it", of, "one hundred ")

#argumen 2
nama = input("Siapa Kamu?")
pekerjaan = input("Saya {Nadsa}, apa pekerjaanmu?")
print("Ahsa bekerja sebagai mafia.")

#hasil 3
anything = float(input ("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

#float 4
angka = float(input("Masukkan angka desimal:"))
print("Nilai yang dimasukkan:", angka)
print("Tipe datanya adalah:", type(angka))

#pytagoras 5
import math
# Input panjang sisi
a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))

# Menghitung sisi miring (hipotenusa)
hypo = math.sqrt(a**2 + b**2)

# Menampilkan hasil
print("Sisi miring segitiga adalah:", hypo)

#Tanpa variabel 6
a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
print("Sisi miring segitiga adalah:", (a**2 + b**2) ** 0.5)

#operator Konkatenasi 7
nama_depan = "Fitria"
nama_belakang = "Rachmadani"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

#replikasi 8
angka = [1, 2, 3]
print(angka * 2)

#konversi 9
angka = 25
teks = str(angka)
print(teks)
print(type(teks))

#Tipe data satu variabel 10
a = 10
b = 3.14
c = "Hello"
d = True

print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # bool

#kuis7.py
# Input nilai dari user
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Operasi matematika
penjumlahan = a + b
pengurangan = a - b
perkalian = a * b
pembagian = a / b

# Output hasil
print("Hasil penjumlahan:", penjumlahan)
print("Hasil pengurangan:", pengurangan)
print("Hasil perkalian:", perkalian)
print("Hasil pembagian:", pembagian)

# Kalimat penutup
print("Selamat kamu sudah pintar matematika")

#kuis8.py
# Input nilai x
x = float(input("Masukkan nilai x: "))

# Inisialisasi nilai y
# Untuk pecahan berulang tak hingga seperti ini, kita bisa menggunakan pendekatan iteratif
# Rumusnya: y = 1/(x + y)
# Tebakan awal
y = 0.0

# Iterasi untuk mendapatkan nilai konvergen
for i in range(100):  # 100 iterasi cukup untuk konvergensi
    y = 1.0 / (x + y)
    
# Tampilkan hasil
print(f"Nilai y = {y}")

#kuis9.py
jam = int(input("Waktu mulai (jam) : "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Waktu acara (menit): "))

# Mengubah waktu ke total menit
total_menit = jam * 60 + menit + durasi

# Menghitung jam dan menit selesai
jam_selesai = total_menit // 60
menit_selesai = total_menit % 60

# Menampilkan hasil
print("Acara berakhir pukul", jam_selesai, ":", menit_selesai)