#kode 1
# Membuat tuple
buah = ("apel", "jeruk", "mangga")

# Menampilkan tuple
print(buah)

#kode 2
# Membuat tuple
mahasiswa = ("Fitria", 19, "Informatika")
# Menggunakan tuple
print("Nama :", mahasiswa[0])
print("Umur :", mahasiswa[1])
print("Jurusan :", mahasiswa[2])

#kode 3
# Tuple awal
buah = ("apel", "jeruk", "mangga")
# Ubah tuple menjadi list
list_buah = list(buah)
# Modifikasi data
list_buah[1] = "pisang"
# Ubah kembali menjadi tuple
buah = tuple(list_buah)
# Tampilkan hasil
print(buah)

#kode 4
# Membuat tuple
angka = (1, 2, 3)
huruf = ("a", "b")

# len() -> menghitung jumlah elemen
print("Jumlah elemen:", len(angka))

# + -> menggabungkan tuple
gabung = angka + huruf
print("Hasil gabung:", gabung)

# * -> mengulang tuple
ulang = angka * 2
print("Hasil pengulangan:", ulang)

# in -> mengecek apakah elemen ada
print(2 in angka)

# not in -> mengecek apakah elemen tidak ada
print(5 not in angka)
#kode 5
# Tuple koordinat
titik = (10, 20)
# Penugasan simultan
x, y = titik
# Menampilkan hasil
print("Nilai x =", x)
print("Nilai y =", y)

#kode 6
# Membuat dictionary
mahasiswa = {
    "nama": "Fitria",
    "umur": 19,
    "jurusan": "Informatika"
}
# Menampilkan dictionary
print(mahasiswa)

#kode 7
# Membuat dictionary
mahasiswa = {
    "nama": "Fitria",
    "umur": 19,
    "jurusan": "Informatika"
}
# Mengakses isi dictionary
print(mahasiswa["nama"])
print(mahasiswa["umur"])
print(mahasiswa["jurusan"])

#kode 8
# Membuat dictionary
mahasiswa = {
    "nama": "Fitria",
    "umur": 19,
    "jurusan": "Informatika"
}
# Mengambil semua key
kunci = mahasiswa.keys()
# Menampilkan key
print(kunci)

#kode 9
# Dictionary data barang
barang = {
    "kode": "B001",
    "nama": "Laptop",
    "harga": 7000000
}
# Menampilkan semua value
print(barang.values())

#kode 10
# Membuat dictionary
mahasiswa = {
    "nama": "Fitria",
    "umur": 19,
    "jurusan": "Informatika"
}
# Mengambil semua item
data = mahasiswa.items()
# Menampilkan item
print(data)

#code 11
# Membuat dictionary
mahasiswa = {
    "nama": "Fitria",
    "umur": 19
}
# Menambahkan data baru
mahasiswa.update({"jurusan": "Informatika"})
# Menampilkan hasil
print(mahasiswa)

#code 12
# Membuat dictionary
mahasiswa = {
    "nama": "Fitria",
    "umur": 19,
    "jurusan": "Informatika"
}
# Menghapus item terakhir
data = mahasiswa.popitem()
# Menampilkan item yang dihapus
print("Data yang dihapus:", data)
# Menampilkan dictionary setelah dihapus
print("Dictionary sekarang:", mahasiswa)

#kode 13
data = {"nama": "Fitria", "umur": 19}
print(data.keys())

#kode 14
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil =", hasil)
except:
    print("Terjadi kesalahan!")

#kode 15
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil =", hasil)
except ValueError:
    print("Input harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol!")
