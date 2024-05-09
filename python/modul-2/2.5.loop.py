# Konsep LOOP

# pengertian loop dalam konteks pemrograman
# loop atau pengulangan dalam pemrograman adalah suatu metode eksekusi program yang dilakukan secara berulang dengan tujuan mempersingkat code.

# python memiliki 3 jenis loop yaitu:
# 1. While Loop
# 2. For Loop
# 3. Nested Loop

# While LOOP
# while loop didalam bahasa pemrograman python dieksekusi statemtnt berkali-kali selama kondisi bernilai benar atau true

# Struktur Syntax
count = 0
while (count < 9):
    print ("nilai count: ", count)
    count = count + 1
print("Selamat tinggal!")

# FOR LOOP
# for loop didalam bahasa pemrograman python memiliki kemampuan untuk mengulangin item dari urutan seperti list atau string

#Struktur Syntax
list_angka = [1,2,3,4,5]

for x in list_angka:
    print(x)

# NESTED LOOP
# nested loop didalam bahasa pemrograman python penggunaan satu lingkaran didalam loop lain (loop didalam loop)

# Struktur Syntax

i = 200

while (i < 100):
    j=2
    while(j <= (i/j)):
        print('Loop dalam loop')
        j = j+1
        i = i+1
print('Selamat tinggal')

#Break & Continue

# Pernyataan break akan mengakhiri proses loop yang ada sedangkan continue akan melewatkan 1 proses loop dan akan tetap berjalanjut ke loop berikutnya.

# Struktur Syntax
for val in "string":
    if val == "i":
        break
    print(val)
print("Loop telah berakhir.")

for val in "string":
    if val == "i":
        continue
    print(val)
print("Loop telah berakhir.")

# Kesimpulan:
# - pada python terdapat tidak jenis loop atau pengulangan yaitu while loop, for loop, dan nested loop
# - while loop akan mengeksekusi pengaulangan ketika kondisi yang kita terapkan bernilai true

# Praktik
count = 0
while(count < 9):
    print("nilai count:", count)
    count = count + 1
print("Selamat tinggal!")

#selain list bisa menggunakan tuple dan dictionary
list_angka = [1,2,3,4,5]

for x in list_angka:
    print("instruksi berjalan....")
    print(x)

print(range(10))

print(list(range(8)))

print(list(range(1,51)))
print(list(range(1,51,3)))

for x in  list (range(1,11)):
    print(x)

# NESTED LOOP\

i = 90

while(i < 100):
    j = 2
    print((i/j))
    while(j <= (i/j)):
        print('Loop')
        j = j+1
        i = i+1
print('selamat tinggal')

#break & Continue
for val in "string":
    if val == "i":
        break
    print(val)
print("Loop telah berakhir.")

for val in "string":
    if val == "i":
        continue
    print(val)
print("Loop telah berakhir.")

# BONUS: FOR ELSE
daftar_murid = ['angga','nico','prastyo']

nama_murid = 'nico'

for nama in daftar_murid:
    if nama == nama_murid:
        print(nama)
        break
else:
    print('Nama murid tidak ditemukan')

# cara kerja for else > saat looping dijalankan data tidak ditemukan maka else akan dijalankan

#BONUS: Pass
for nama in daftar_murid:
    pass


# Latihan
# Buatlah operasi loop yang akan mencetak angka GENAP dari 1-120
# Lalu gunakan statement continue agar operasi tidak mencetak angka 12, 56 dan 78
# Dan juga gunakan statement break agar operasi berhenti hanya sampai di angka 100

# list_angka = range(1)

for i in range(1, 121):
    if i % 2 == 0:
        if i == 12 or i == 56 or i == 78:
            continue
        print(i)
    if i == 100:
        break
