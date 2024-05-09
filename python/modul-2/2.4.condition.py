# Konsep
# Pengertian Condition dalam konteks pemrograman

# condition atau kondisi dalam pemrograman adalah proses penentuan keputusan berdasarkan keadaan yang didefinisikan atau disebut dengan conditional statement

# ini berguna untuk menyusun alur logika pemrograman agar sesuai dengan yang semestinya

# Fungsi if

# fungsi if merupakan percabangan yang digunakan untuk menentukan tindakan apa yang dilakukan sesuai dengan konsisi tertentu

#Struktur syntax
score = 50

if score > 45:
    print("Nilai lebih bedar dari 45")

#Fungsi IF ELSE

# fungsi if else merupakan percabangan yang tidak hanya digunakan untuk menentukan tindakan berdasarkan suatu kondisi tertentu. tetapi juga menentukan tindakan jika kondisi yang dinyatakan tidak sesuai

# Struktur Syntax
score = 78
if score > 75:
    print('Lulus')
else:
    print('Tidak Lulus')

#Fungsi IF ELIF ELSE

# fungsi if elif else merupakan percabangan tidak hanya bisa untuk dua kondisi, naum bisa untuk tidak, empat, bahkan lebih kondisi percabangan. Fungsi if elif else digunakan untuk lebih dari dua logika percabangan

#Struktur Syntax
score = 78
if score >= 85:
    print('Predikat A/Memuaskan')
elif score >= 75:
    print('Predikat B/Bagus')
else:
    print('Tidak Lulus')

# Kesimpulan

# - Condition atau kondisi berguna untuk menyusun alur logika pemrograman agar sesuai dengan yang semestinya
# - condition memiliki tiga pembagian yaitu if kemudian if else dan if elif else yang dibedakan dari seberapa kompleks pengkodisian yang ada.

# Praktik
jumlah_penumpang = 1

if jumlah_penumpang > 10:
    # pass #di python dapat menggunakan keyword pass untuk memberentikan code
    print("Mobil berjalan...")

if jumlah_penumpang < 10:
    print("Mobil menunggu penumpang lain")

print("Di luar condition")

kelas = 1 #output: Predikat A/bagus
# kelas = 3 output: Predikat A/Memuaskan
score = 90

if kelas > 1:

    if score >= 85:
        print('Predikat A/Memuaskan')
    elif score >= 75:
        print('Predikat B/Bagus')
    else:
        print('Tidak lulus')

else:

    if score >= 80:
        print('Predikat A/bagus')
    else: print('tidak Lulus')        


num = float(input("Masukkan angka: "))
if num >= 0:
    
    if num == 0:
        print("Nol")
    else:
        print("Angka positif")