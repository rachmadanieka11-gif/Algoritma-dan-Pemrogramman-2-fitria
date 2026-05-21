# kode 1
angka = [4, 2, 3, 1]

for i in range(len(angka)):
    for j in range(len(angka)-1):
        if angka[j] > angka[j+1]:
            # tukar posisi
            angka[j], angka[j+1] = angka[j+1], angka[j]

print(angka)

#kode 2
data = input("Masukkan angka: ")
angka = list(map(int, data.split()))

for i in range(len(angka)):
    print(f"Iterasi ke-{i+1}")
    for j in range(len(angka) - 1):
        if angka[j] > angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]
    print(angka)

print("Hasil akhir:", angka)

#kode 3
angka = [4, 2, 3, 1]
angka.sort(reverse=True)
print(angka)

#kode 4
data = [3, 1, 4, 2]
data.sort()
print(data)  # hasil: [1, 2, 3, 4]

#kode 5
list_1 = [1]
list_2 = list_1 
list_1[0] = 2
print(list_2)

#kode 6
my_list = [10,8,6,4,2]
new_list = my_list[1:3]
print(new_list)

#kode 7
my_list = [10,8,6,4,2]
new_list = my_list[1:-1]
print(new_list)

#kode 8
my_list = [10,8,6,4,2]
new_list = my_list[-1:1]
print(new_list)

#kode 9
my_list = [10,8,6,4,2]
new_list = my_list[3:]
print(new_list)

#kode 10
my_list = [10,8,6,4,2]
new_list = my_list[:3]
print(new_list)

#kode 11
data = [1, 2, 3, 4]
salinan = data[:]
print(salinan)

#kode 12
data = [1, 2, 3, 4, 5]
del data[1:4]
print(data)

#kode 13
data = [1, 2, 3]
del data[:]
print(data)

#kode 14
data = [1, 2, 3]
del data
print(data)

#kode 15
data = [1, 2, 3, 4]
print(2 in data)

#kode 16
angka = [10, 20, 30]

if 40 not in angka:
    print("Angka 40 tidak ada")

#kode 17
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#kode 18
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

#kode 19
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemen ditemukan pada index ke-", i)
else:
    print("Tidak ada di dalam list")
    
#kode 20
tebakan = [3, 7, 11, 42, 34, 49]
hasil = [5, 9, 11, 42, 3, 49]

benar = 0

for angka in tebakan:
    if angka in hasil:
        benar += 1

print("Jumlah tebakan yang benar:", benar)

#kode 21
data = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unik = []

for angka in data:
    if angka not in unik:
        unik.append(angka)

print("List tanpa duplikat:", unik)    