#variabel local
def tambah():
    a = 10
    b = 20
    return a + b
print(tambah()) # 30

#variable di luar
bilangan = 2
def perkalian_bilangan(x):
    return x * bilangan
print(perkalian_bilangan(8))

#variable di luar 2
def perkalian_bilangan(x):
    bilangan = 10
    return x * bilangan
print(perkalian_bilangan(8))

#global key
bilangan = 2
print(bilangan)

def return_bilangan ():
    global bilangan
    bilangan = 15
    return_bilangan

print(return_bilangan())   
print(bilangan) 

#IMT
def hitung_imt(berat, tinggi):
    return berat / (tinggi ** 2)

while True:
    berat = float(input("Masukan berat badan (kg): "))
    tinggi_cm = float(input("Masukan tinggi badan (cm): "))

    tinggi = tinggi_cm / 100  # konversi ke meter
    imt = hitung_imt(berat, tinggi)
    
    if imt < 18.5:
        hasil = "Kurus"
    elif imt < 25:
        hasil = "Normal"
    elif imt < 30:
        hasil = "Gemuk"
    else:
        hasil = "Obesitas"

    print("IMT:", round(imt, 2))
    print("Kategori:", hasil)

    if hasil == "Normal":
        print("Selamat! IMT Anda sudah normal.")
        break
    else:
        print("Belum normal, silakan input lagi.\n")

#fungsi segitiga 1
def cek_segitiga(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True 

print(cek_segitiga(1,1,1)) # True
print(cek_segitiga(1,1,3)) # False 

#fungi segitiga 2
def cek_segitiga(a,b,c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(cek_segitiga(1,1,1)) # True
print(cek_segitiga(1,1,3)) # False

#fungsi segitiga 3
def cek_segitiga(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(cek_segitiga(1,1,3)) # False 

#fungsi faktorial 
def faktorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

n = int(input("Masukan angka: "))
print(n, "! = ", faktorial(n))

#fungsi fibonacci
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem_1, elem_2 = 1, 1
    hasil_jumlah = 0 #untuk menyimpan hasil penjumlahan

    for i in range(n - 2):
        #proses penjumlahan
        hasil_jumlah = elem_1 + elem_2

        #tukar elemen
        elem_1 = elem_2
        elem_2 = hasil_jumlah
    return hasil_jumlah
#test
for n in range(1, 10):
    print(n , "-> ", fibonacci(n))

#rekursif fakctorial
def faktorial(n):
    if n == 4:
        return 1
    else:
        return n * faktorial(n - 1)
    
print(faktorial(6))    

#rekursif fibonacci
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#test
for n in range(1, 8):
    print(fibonacci(5))