kata = ["apel", "jeruk", "mangga"]
kapital = [k.upper() for k in kata]

print("List awal:", kata)
print("Huruf besar:", kapital)

#kode 2
buku = [
    ["Matematika", 50000],
    ["Bahasa Inggris", 60000],
    ["IPA", 55000]
]
# Menampilkan data buku
for b in buku:
    print("Judul:", b[0], "- Harga:", b[1])

#kode 3
# Membuat list multidimensi
data = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

# Menampilkan semua isi
print("Isi data:")
for lapisan in data:
    for baris in lapisan:
        print(baris)
    print()

# Mengakses elemen tertentu
print("Elemen tertentu:", data[0][1][0])  # 3

# Menghitung jumlah semua elemen
total = 0
for lapisan in data:
    for baris in lapisan:
        for angka in baris:
            total += angka

print("Total:", total)

#kode 4
def tambah(a, b):
    hasil = a + b
    print("Hasil:", hasil)

tambah(3, 5)

#kuis 1
angka = [x for x in range(1, 11) if x % 2 == 0]
hasil = [x * 3 for x in angka]
print(hasil)

#kuis 2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for baris in matrix:
    print(baris)

#kuis 3
data = [[2,4],[6,8],[10,12]]
flatten = [x for sublist in data for x in sublist]
print(flatten)

#slice 4
def luas(panjang, lebar):
    return panjang * lebar

hasil = luas(8, 5)
print("Luas:", hasil)