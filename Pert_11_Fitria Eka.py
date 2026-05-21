#kode 1
def salam():
    print("Halo")

salam()

#kode 2
def cek(status):
    if status == False:
        print("Status salah")
        return

cek(False)

#kode 3
def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print(hasil)

#kode 4
def fungsi_malas():
    return 123

x = fungsi_malas()
print("Hasil dari fungsi malas adalah: ", x)

#kode 5
def contoh():
    return

hasil = contoh()
print(hasil)

#kode 6
def tampilkan(data):
    for item in data:
        print(item)

angka = [1, 2, 3, 4]

tampilkan(angka)

#kode 7
def luas_persegi(sisi):
    return sisi * sisi

print(luas_persegi(4))

#kode 8
def buat_list():
    data = [1, 2, 3, 4]
    return data

hasil = buat_list()

print(hasil)

#kode 9 Kuis 23
def cek_tahun_kabisat(tahun):
    # Tahun kabisat:
    # habis dibagi 400
    # atau habis dibagi 4 tetapi tidak habis dibagi 100
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False


# List data uji (tahun yang akan dicek)
data_uji = [2000, 2004, 1900, 2023, 2024, 2100]

# List hasil yang diharapkan
data_hasil = [True, True, False, False, True, False]


# Proses pengujian
for i in range(len(data_uji)):
    hasil_program = cek_tahun_kabisat(data_uji[i])

    if hasil_program == data_hasil[i]:
        print(f"Tahun {data_uji[i]} -> Benar ")
    else:
        print(f"Tahun {data_uji[i]} -> Salah ")
        
#kode 10 Kuis 24        
def cek_tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False


def jumlah_hari(tahun, bulan):
    # Jumlah hari tiap bulan
    hari_per_bulan = [31, 28, 31, 30, 31, 30,
                       31, 31, 30, 31, 30, 31]

    # Jika Februari dan tahun kabisat
    if bulan == 2 and cek_tahun_kabisat(tahun):
        return 29

    return hari_per_bulan[bulan - 1]


# Contoh penggunaan
print(jumlah_hari(2024, 2))   # 29
print(jumlah_hari(2023, 2))   # 28
print(jumlah_hari(2025, 4))   # 30
print(jumlah_hari(2025, 12))  # 31

#kode 11 Kuis 25
def cek_tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False


def jumlah_hari(tahun, bulan):
    hari_per_bulan = [31, 28, 31, 30, 31, 30,
                       31, 31, 30, 31, 30, 31]

    if bulan < 1 or bulan > 12:
        return None

    if bulan == 2 and cek_tahun_kabisat(tahun):
        return 29

    return hari_per_bulan[bulan - 1]


def hari_dalam_tahun(tahun, bulan, hari):
    # Validasi bulan
    if bulan < 1 or bulan > 12:
        return None

    # Ambil jumlah hari pada bulan tersebut
    max_hari = jumlah_hari(tahun, bulan)

    # Validasi hari
    if hari < 1 or hari > max_hari:
        return None

    # Jumlah hari tiap bulan
    hari_per_bulan = [31, 28, 31, 30, 31, 30,
                       31, 31, 30, 31, 30, 31]

    # Jika tahun kabisat, Februari = 29
    if cek_tahun_kabisat(tahun):
        hari_per_bulan[1] = 29

    # Hitung total hari
    total = sum(hari_per_bulan[:bulan - 1]) + hari

    return total


# =========================
# Data uji
# =========================

data_uji = [
    (2024, 1, 1),
    (2024, 2, 29),
    (2023, 12, 31),
    (2023, 2, 29),   # tidak valid
    (2025, 13, 10),  # bulan tidak valid
]

# Hasil yang diharapkan
data_hasil = [
    1,
    60,
    365,
    None,
    None
]

# =========================
# Pengujian
# =========================

for i in range(len(data_uji)):
    tahun, bulan, hari = data_uji[i]

    hasil_program = hari_dalam_tahun(tahun, bulan, hari)

    if hasil_program == data_hasil[i]:
        print(f"{data_uji[i]} -> Benar ")
    else:
        print(f"{data_uji[i]} -> Salah ")
        
#kode 12 Kuis 26
def cek_prima(nilai):
    # Bilangan prima harus lebih besar dari 1
    if nilai <= 1:
        return False

    # Mengecek pembagi selain 1 dan dirinya sendiri
    for i in range(2, nilai):
        if nilai % i == 0:
            return False

    return True


# Contoh penggunaan
print(cek_prima(2))   # True
print(cek_prima(7))   # True
print(cek_prima(10))  # False
print(cek_prima(1))   # False

#kode 13 Kuis 27
def cek_prima(nilai):
    # Bilangan prima harus lebih besar dari 1
    if nilai <= 1:
        return False

    # Mengecek apakah memiliki pembagi selain 1 dan dirinya sendiri
    for i in range(2, nilai):
        if nilai % i == 0:
            return False

    # Jika tidak ada pembagi lain
    return True

# Contoh pengujian
print(cek_prima(2))    # True
print(cek_prima(3))    # True
print(cek_prima(4))    # False
print(cek_prima(17))   # True
print(cek_prima(20))   # False        

#kode 14 Kuis 28
def Liter100km_ke_mpg(liter):
    # 100 km = 100000 meter
    mil = 100000 / 1609.344
    
    # Mengubah liter menjadi galon
    galon = liter / 3.785411784

    return mil / galon

def mpg_ke_Liter100km(mil):
    # Mengubah mil menjadi km
    km100 = (mil * 1609.344) / 100000

    # 1 galon = 3.785411784 liter
    liter = 3.785411784

    return liter / km100

print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))

print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))