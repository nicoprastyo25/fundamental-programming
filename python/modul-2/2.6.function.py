# Konsep Function
# Pengertian Function dalam konteks pemrograman

# function atau fungsi merupakan sebuah blok kode yang memiliki tujuan spesifik dan akan dieksekusi ketika fungsi tersebut dipanggil dalam sebuah instruksi kode.

# Deklarasi function
# - kata kunci def yang menjadi pertanda bahwa blok kode program adalah sebuah fungsi
# - lalu disusul dengan nama fungsi yang kita buat
# - parameter yang akan diterima oleh fungsi yang kita buat(tidak wajib)
# - blok kode yang kita tulis perintah-perintah yang harus dilakukan oleh sebuah fungsi

# Fungsi non-parameter adalah fungsi yang tidak disertai parameter adalah pendeklarasian fungsi tersebut

#Struktur Syntax
def halo_dunia():
    var = "hallo, dunia"
    print(var)

# Pemanggilan fungsi
halo_dunia()

# fungsi parameter adalah fungsi yang disertai parameter dalam pendeklarasian fungsi tersebut.

#Struktur syntax
def selamat_datang(nama):
    var = f'Halo {nama}, Welcome '
    print(var)

# Pemanggilan fungsi
selamat_datang('Nico') 

# Fungsi anonim adalah fungsi yang dibuat tanpa nama dengan menggunakan keyword lambda.
# STruktur Syntax
double = lambda x: x * 2
print(double(5))

# Praktik

def halo_dunia():
    var = "hallo, dunia"
    print(var)

# Pemanggilan fungsi
halo_dunia()


def selamat_datang(nama):
    var = f'Halo {nama}, Welcome '
    print(var)

selamat_datang('Nico')

def selamat_datang(nama, kota):
    var = f'Halo {nama} dari {kota}, Welcome '
    print(var)

selamat_datang('Nico', 'tangerang selatan')
selamat_datang(kota='tangerang selatan', nama='nico')

def getNama (*daftar_nama):

    var = 'Halo '
    for nama in daftar_nama:
        var += nama + ', '

    var += 'Welcome!' # var = var + 'welcome'
    print(var)

getNama('nico','prastyo','mira','ranti')

#anonim
double = lambda x: x * 2
print(double(5))

#BONUS: Docstring
def selamat_datang(nama):
    '''
    ini adalah fungsi untuk menyapa
    nama yang telah disebutkan
    '''
    var = f'Halo {nama}, welcome!'
    print(var)

selamat_datang('nurul')
print(selamat_datang.__doc__)

# BONUS: Scope & Return

def operasi(a,b,c):

    op1 = a + b
    op2 = op1 // c

    return op2

hasil = operasi(a=10, b=5, c=1) #C=1 samadengan nilai default
print(hasil)

def operasi(a,b,c=1):

    op1 = a + b
    op2 = op1 // c

    return op2

hasil = operasi(a=10, b=5)
print(hasil)

# Scope
a = 2 #a sama dengan Scope luar
b = 1
x = 100
def operasi(a,b,c=1):

    op1 = a + b # a sama dengan Scope dalam
    op2 = op1 // c

    print('a didalam function:', a)
    print(x)
    return op2

hasil = operasi(a=10, b=5)
print(hasil)

print ('a di luar function:', a)
print ('b di luar function:', 1)

# Latihan
# Buatlah fungsi yang akan mengevaluasi apakah modulus dari hasil kali 2 angka yang diterima bernilai 0 atau tidak
# Gunakan statement return untuk mengembalikan nilai tersebut lalu cetak hasilnya
# Beri nama cek_modulus() pada fungsi tersebut


def cek_modulus(angka1, angka2):
        opm = angka1 % angka2
        return opm
hasil = cek_modulus(angka1=12, angka2=8)
print(hasil)

