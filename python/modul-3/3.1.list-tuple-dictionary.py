# KONSEP LIST TUPLE & DICTIONARY

# list

# Apa itu list?
# list adalah tipe data yang tesedia dalam bahasa pemrograman python yang dapat ditulis dalam bentuk daftar nilai yang dipisahkan tanda koma antara nilai dan berada dalam tanda kurung siku [].

# Contoh Penerapan

# ini adalah instruksi untuk membuat list
list1 = ["apple","banana","watermelon"]
list2 = [1,2,3,4,5,6]
list3 = [True,False,False]
list4 = ["abc",10,True,40,"Male"]

# Mengakses list
# Pada list kita dapat mengakses element yang ada dengan mendeklarasikan indeks dari elemen yang ingin kita akses. pada list urutan indeks elemennya dimulai dari indeks-0 dan seterusnya

# Contoh penerapan
# ini adalah instruksi untuk mengakses list
fruit_list = ["apple","banana","watermelon","orange","mango"]
fruit_list[1] #output: banana
fruit_list[1:4] #output: banana, watermelon, orange
fruit_list[-2] #output: orange, mango

# Mengganti List
# pada list juga kita dapat mengubah atau mengganti satu atau lebih nilai dari sebuah element dari list

# Contoh penerapan
# Ini adalah instruksi untuk mengganti list
fruit_list = ["apple","banana","watermelon","orange","mango"]
fruit_list[2] = "avocado"

# Menambah list
# ada beberapa cara untuk menambah elemen dari sebuah list. untuk melakukannya kita dapat menggunakan method seperti berikut:
# - append(): menambahkan item list kearah kanan
# - insert(): Menambahkan item pada urutan indeks yang diinginkan
# - extend(): Menambah item list dengan list lain

# Contoh penerapan
# Ini adalah instruksi untuk menambah list
fruit_list = ["apple", "banana"]
fruit_list.append("watermelon") # output: "apple","banana","watermelon"

fruit_list = ["apple", "banana","watermelon"]
fruit_list.insert(1, "orange") # output: "apple","orange","banana","watermelon"

fruit_list1 = ["apple", "orange"]
fruit_list2 = ["banana", "watermelon"]
fruit_list1.extend(fruit_list2) # output: "apple","orange","banana","watermelon"

# Menghapus List
# kita dapat menghapus elemen item dari sebuah list dengan menggunakan beberapa method seperti remove(), pop(), ataupun del.
fruit_list = ["apple","orange","banana","watermelon"]
fruit_list.remove("orange") #output: "apple", "banana", "watermelon"

fruit_list = ["apple","orange","banana","watermelon"]
fruit_list.pop(1) #output: "apple", "banana", "watermelon"

fruit_list = ["apple","orange","banana","watermelon"]
del fruit_list[1] #output: "apple", "banana", "watermelon"

# KONSEP TUPLE

# Apa itu tuple?
# tuple adalah tipe data yang tersedia dalam bahasa pemrograman python yang dapat ditulis dalam bentuk daftar nilai yang dipisahkan koma (item) antara nilai dan berada dalam tanda kurung(). berbeda dengan list, tuple bersifat permanen atau immutable. arti immutable adalah value/elemen yang sudah dibuat pda tuple itu tidak bisa diubah

# Contoh Penerapan:

# ini adalah instruksi untuk membuat tuple
tuple1 = ("apple", "banana", "watermelon")
tuple2 = (1,3,4,5,6,7)
tuple3 = (True, False, False)
tuple4 = ("abc",10,True,40,"male")

# mengakses tuple
# pada tuple kita dapat mengakses element yang ada dengan mendeklarasikan indeks dari element yang ingin kita akses. tidak ada perbedaan dengan list.
fruit_list = ("apple","banana","watermelon","orange","mango")
fruit_list[1] #output: banana
fruit_list[1:4] #output: banana, watermelon, orange
fruit_list[-2] #output: orange, mango

# Apa itu immutable?
# tidak seperti list, tuple bersifat immutable. yang berarti elemen yang ada pada tuple tidak bisa diubah. ini berguna untuk menyimpan nilai-nilai yang semestinya tidak berubah semisal konstanta atau e pada matematika

# Contoh Penerapan:
# ini adalah instruksi gagal ketika mengganti tuple
fruit_list = ["apple","banana","watermelon","orange","mango"]
fruit_list[1] = "banana"
# TypeError: 'tuple' object does not support item assignment

# Menghapus tuple
# ini adalah instruksi gagal ketika menghapus tuple
fruit_list = ["apple","banana","watermelon","orange","mango"]
del fruit_list[1]
# TypeError: 'tuple' object does not support item deletion

# DICTIONARY
# apa itu dictionary?
# dictionary adalah tipe data yang tersedia dalam bahasa pemrograman python yang dapat ditulis dalam bentuk data dengan struktur key-value. bukan daftar nilai seperti pada list ataupun tuple dan berada dalam tanda kurung kurawal{}.

# Apa itu dictionary?
# Contoh penerapan

# ini adalah instruksi untuk membuat dictionary
fruit_dict = {
    'nama':'pisang',
    'jenis': 'ambon',
    'kode' : 891,
    'harga' : 20.000
}

# Operasi pada dictionary

# operasi yang ada pada dictionary sama dengan operasi yang bisa dilakukan pada list dantuple yaitu mengakses, mengganti, menambah dan menghapus.

# Kesimpulan
# list adalah tipe data dalam bentuk daftar nilai yang dipisahkan tanda koma antara nilai dan berada dalam tanda []
# berbeda dengan list, tuple bersifat immutable sehingga lebih aman dan cepat dan berada dalam tanda()
# dictionary adalah tipe data yang ditulis dalam bentuk data dengan struktur key-value dan berada dalam tanda{}

# Praktik
# List
list1 = ["apple", "banana", "watermelon"]
list2 = [8,3,4,5,6,7]
list3 = [True, False, False]
list4 = ["abc",10,True,40,"male"]
list5 = [list1,list2,list3,list4]

print(list1 + list2)

list2.sort()
print(list2)

list1.reverse()
print(list1)

list3 = list2.copy()
print(list3.count(2))

# mengakses list
fruit_list = ["apple","banana","watermelon","orange","mango", "cerry", "pineapple"]
# print(fruit_list[1])
# print(fruit_list[1:4])
# negative indexing
# print(fruit_list[-2])
# print(fruit_list[-3:4])
# print(fruit_list[-3])

# print(fruit_list[-5:])
fruit_list[2] = "avocado"
print(fruit_list)
#membership test
print('avocado' in fruit_list)
print('watermelon' not in fruit_list)

fruit_list = ["apple", "banana", "watermelon"]
fruit_list.append("mango")
print(fruit_list)

fruit_list = ["apple", "banana", "watermelon"]
fruit_list.insert(1,"mango")
print(fruit_list)

fruit_list1 = ["apple", "banana", ]
fruit_list2 = ["watermelon", "mango"]
fruit_list1.extend(fruit_list2)
print(fruit_list1)

# Cara menghapus elemen
fruit_list = ["apple","orange","banana","watermelon"]
fruit_list.remove("orange") #output: "apple", "banana", "watermelon"

fruit_list = ["apple","orange","banana","watermelon"]
fruit_list.pop(1) #output: "apple", "banana", "watermelon"

fruit_list = ["apple","orange","banana","watermelon"]
del fruit_list[1] #output: "apple", "banana", "watermelon"

#TUPLE
# ini adalah instruksi untuk membuat tuple
tuple1 = ("apple", "banana", "watermelon")
tuple2 = (1,3,4,5,6,7)
tuple3 = (True, False, False)
tuple4 = ("abc",10,True,40,"male")

fruit_tuple = ("apple","banana","watermelon","orange","mango")
print(fruit_list[1]) #output: banana
print(fruit_list[1:4]) #output: banana, watermelon, orange
print(fruit_list[-2]) #output: orange, mango

# del fruit_tuple[1]

for fruit in fruit_tuple:
    print("Nama Buah:", fruit)

# Dictionary
fruit_dict = {
    'nama': 'pisang',
    'jenis' : 'ambon',
    'kode' : 891,
    'harga' : 20000
}

print(fruit_dict['jenis'])

fruit_dict['jenis'] = 'jeruk'

print(fruit_dict)

fruit_dict['price'] = 3000

print(fruit_dict)

for key, value in fruit_dict.items():
    print(key,":",value)

for key in fruit_dict.keys():
    print(key,":",fruit_dict["harga"])

fruit_dict = [
    {
    'nama': 'pisang',
    'jenis' : 'ambon',
    'kode' : 891,
    'harga' : 20000
},{
    'nama': 'pisang',
    'jenis' : 'ambon',
    'kode' : 891,
    'harga' : 20000
}
]
print(fruit_dict)


# Bonus: Set/di matematika disebut Himpunan
A = {1,2,3,4,5}
B = {4,5,6,7}

#Union
print( A | B)

#Intersection
print( A & B)

#difference
print( A - B)
print( B - A)

#Symmetric difference
print( A ^ B)

#Latihan
# Buatlah 2 buah dictionary yang memuat informasi 10 murid dan informasi 10 karyawan
# Lalu cetak data murid dan karyawan yang berada di-index 2 dan 9
# Setelah itu cetak semua data yang ada di dictionary tersebut dengan for loop

dict_murid = [
{
    'nim' : 2001,
    'nama': 'nico',
    'kelas' : 12

},
{
    'nim' : 2002,
    'nama': 'tomi',
    'kelas' : 12

},
{
    'nim' : 2003,
    'nama': 'arip',
    'kelas' : 12

},
{
    'nim' : 2004,
    'nama': 'miranti',
    'kelas' : 12

},{
    'nim' : 2001,
    'nama': 'nico',
    'kelas' : 12

},
{
    'nim' : 2002,
    'nama': 'tomi',
    'kelas' : 12

},
{
    'nim' : 2003,
    'nama': 'arip',
    'kelas' : 12

},{
    'nim' : 2001,
    'nama': 'nico',
    'kelas' : 12

},
{
    'nim' : 2002,
    'nama': 'tomi',
    'kelas' : 12

},
{
    'nim' : 2003,
    'nama': 'arip',
    'kelas' : 12

}]
dict_karyawan = [
    {
    'nik' : 3001,
    'nama': 'reza',
    'status' : 'tetap'

},
{
    'nik' : 3002,
    'nama': 'agus',
    'status' : 'tetap'

},
{
    'nik' : 3003,
    'nama': 'mircan',
    'status' : 'tetap'

},
{
    'nik' : 3004,
    'nama': 'prastyo',
    'status' : 'tetap'

},
{
    'nik' : 3002,
    'nama': 'agus',
    'status' : 'tetap'

},
{
    'nik' : 3003,
    'nama': 'mircan',
    'status' : 'tetap'

},
{
    'nik' : 3002,
    'nama': 'agus',
    'status' : 'tetap'

},
{
    'nik' : 3003,
    'nama': 'mircan',
    'status' : 'tetap'
}
]

# print(dict_murid[-2:9])
# print(dict_karyawan[-2:9])

print("Daftar Murid:")
for murid in dict_murid:
    print(f"NIM: {murid['nim']}, Nama: {murid['nama']}, Kelas: {murid['kelas']}")

print("\nDaftar Karyawan:")
for karyawan in dict_karyawan:
    print(f"NIK: {karyawan['nik']}, Nama: {karyawan['nama']}, Status: {karyawan['status']}")


# Membuat list gabungan dengan menambahkan informasi tipe (Murid atau Karyawan)
data_gabungan = []

for murid in dict_murid:
    murid['tipe'] = 'Murid'
    data_gabungan.append(murid)

for karyawan in dict_karyawan:
    karyawan['tipe'] = 'Karyawan'
    # Menambahkan 'kelas' dengan nilai default 'N/A' untuk karyawan
    karyawan['kelas'] = 'N/A'
    # Mengganti 'nik' dengan 'nim' untuk konsistensi
    karyawan['nim'] = karyawan.pop('nik')
    data_gabungan.append(karyawan)

# Mencetak data gabungan
print("Daftar Gabungan (Murid dan Karyawan):")
for data in data_gabungan:
    print(f"Tipe: {data['tipe']}, NIM/NIK: {data['nim']}, Nama: {data['nama']}, Kelas: {data['kelas']}, Status: {data.get('status', 'N/A')}")