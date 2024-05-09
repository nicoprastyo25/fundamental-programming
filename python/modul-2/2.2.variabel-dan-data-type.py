# Konsep Variable

# Apa itu Variable?
# Variable adalah lokasi memori yang dicadangkan untuk menyimpan nilai-nilai di suatu pemrograman

# Contoh:
# nama variabel = value/nilai
# variabel_saya = "Nilai-nilai yang disimpan di variabel"

# Aturan penulisan variable python
# - Karakter pertama harus berupa huruf atau garis bawah/underscore _.
# - Karakter selanjutnya dapat berupa huruf, garis bawah/underscore _ atau angka.
# - karakter pada nama variable bersifat sensitif (case-sensitif) Artinya huruf kecil dan huruf besar dibedakan. sebagai contoh, variabel namaDepan dan namadepan adalahvariabel

# Aturan penulisan variable python contoh:
# variable_saya (BENAR)
# variable123 (BENAR)
# VariabelSaya (BENAR)
# @variable (SALAH)

# Contoh penggunaan variable dalam pemrograman python
nama = "Nico prastyo"   #nilai awal
print(nama)             #mencetak nilai nama

# value(nico prastyo) disimpan pada variabel (nama) lalu di print/tampilkan menggunakan variable nama


# Konsep Data Type
#Data type adalah suatu media atau jenis memori pada komputer yang digunakan untuk menampung informasi semisal teks atau angka numerik.

umur = 20 #nilai awal
print(umur) #mencetak nilai umur
type(umur) #mengecek tipe data umur

umur2 = "dua puluh" #nilai setelah diubah
print(umur2)        #Mencetak nilai umur
type(umur2)         #mengecek tipe data umur

# Data Type Python
# Text Type : String (str)
# Number Type : Integer (int), Float dan Hexadecimal contoh 30(int) 0.75(float) 3/4(hexadecimal)
# Binary Type : Boolean (True or False)
# Sequence Type : List, Tuple, Set dan Dictionary

# Didalam pemrograman python, variable mempunyai sifat yang dinamis
# Artinya variable Python tidak perlu di deklarasikan data type tertentu dan variable python dapat diubah saat program dijalankan

# Contoh penggunaan data type dalam pemrograman python

# Tipe data list
print ([1,2,3,4,5])
print(["satu","dua","tiga"])

# Tipe data tuple
print((1,2,3,4,5))
print(("satu","dua","tiga"))

# Tipe data Dictionary
print({"nama":"Nico", "umur":20})

# Praktik
angka = 10
print(angka)

angka = 100
print(angka)

angka = 0.1
print(angka)

nim, nama, email = 140021, "Nico", "nico@gmail.com"
print(nim)
print(nama)
print(email)

angka1 = angka2 = angka3 = 100
print(angka1)
print(angka2)
print(angka3)

# CONSTANTA = memuat nilai yang konsisten tidak berubah
# harus menggunakan huruf BESAR
PI = 3.14
GRAVITY = 9.8

# Naming
nama_variable = "Nico prastyo"
NAMA_VARIABLE = "PRASTYO NICO"

print(nama_variable)
print(NAMA_VARIABLE)
# Dilarang: !,@,#,$,% digit 0-9 diawal

#Literals
nomor_biner = 0b1010
nomor_desimal = 100
nomor_float = 1.5e2

print(nomor_biner)
print(nomor_desimal)
print(nomor_float)

#Menampilkan Type Variable
a = 5
print(type(a))

b = 2.0
print(type(b))

c = 4/5
print(type(c))

a = float(a)
print(type(a))

c = 8/5
c = c.__ceil__()
print(c)

c = 8/5
c = c.__float__()
print(c)

c = 8/5
print(c)

#STRING
s = "ini adalah string single-line"
print(type(s))

s = '''
    ini adalah string
    namun bukan single-line melainkan multi-line
'''
print(type(s))

s = s.lower()
print(s)

s = s.upper()
print(s)

s = s.replace('ADALAH','MERUPAKAN')
print(s)

nama = "Nico"
s = f"Nama saya adalah {nama}"
print(s)

nama = "budi"
s = "Nama saya adalah {}".format(nama)
print(s)

#TRUE AND FALSE (BOOLEAN)
b = True
print(type(b))

print(b == 1)
print(b == 0)

# LOGIKA
# TRUE and TRUE = TRUE
# FALSE and TRUE = FALSE
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True & True)
print(True & False)
print(False & True)
print(False & False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(True | True)
print(True | False)
print(False | True)
print(False | False)

#List, Tuple & Dictionary (memuat data)
l = [1, 2.2, "python"]
print(type(l))

t = ((1, 2.2, "python"))
print(type(t))

d = {
    "key1"  : "value1",
    "key2" : "value2"
}

#Latihan
# Buatlah 2 variable yang memuat string
# Variable 1 memuat "Hello, "
# Variable 2 memuat "Python!"
# Lalu gabungkan kedua string tersebut dan tampung di variable hasil seperti ini
# hasil = variable1 + variable2
# Pastikan string yang ada bersifat upper-case
# Lalu cek apa Data Type dari variable hasil tersebut!

variable1 = "Hello, "
variable2 = "Python!"

hasil = variable1 + variable2

print(hasil)