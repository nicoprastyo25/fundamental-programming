# KONSEP
# Apa itu Class?
# class adalah blueprint dari sekumpulan objek yang akan dibuat. sebagaimana blueprint atau cetak biru padea umumnya
# misal dengan kelas Kucing. kita bisa membuat objek-objek seperti kucing anggora, kucing persia dan Kucing siam.

# Membuat class di python
# contoh penerapan,

# ini adalah contoh class
# class Cat:
    #isi kelas akan memuat attribute dan method dari si kucing 
    # """ini adalah kelas untuk membuat objek-objek kucing"""
    # pass

# Apa itu Object?
# Object adalah hasil buatan yang merujuk pada kelas. saat kelas didefinisikan, maka definisi tersebut akan dibawa oleh objek tersebut

# Membuat object di python
# Contoh penerapan,

#ini adalah contoh object
# Persia = Cat()

# Membuat object anggora dan persia dari class Cat.
# Nama class diawali dengan huruf kapital.
# class Cat:
# Metode __init_() berfungsi untuk mendefinisikan atribute sejak pertama kali class dipanggil dikenal dengan istilah konstruktor.
    # def __init__(self, nama, tipe):
    #     self.nama = name
    #     self.tipe = type
# Kedua objek yang sudah dibuat yaitu anggora dan persia memiliki behaviour yang sama yaitu run()
#     def run(self):
#         print(f"Kucing {self.nama} berlari...")

# kinako = Cat("Kinako", "Anggora")
# minto  = Cat("Minto","Persia")

# Kita bisa mendefinisikan lebih dari satu method sebagai perilaku/behaviour dari object yang akan kita buat.
    # def run(self):
    #     print(f"Kucing {self.nama} berlari...")

    # def play(self):
    #     print(f"Kucing {self.nama} bermain dengan kucing lainnya...")

# KESIMPULAN
# OOP merupakan salah satu teknik yang popular untuk menyelesaikan masalah-masalah bahasa pemrograman
# Mendukung ide agar file-file python yang kita miliki lebih understandable dan reusable
# class adalah blueprint dar sekumpulan objek yang akan dibuat dan sebagaimana blueprint atau cetak biru pada umumnya

# Praktik
class Cat:
    # '''
    # ini adalah class untuk membuat objek kucing
    # melalui kelas ini kita bisa mendefinisikan nama dan juga tipe dari kucing yang dibuat
    # '''

    spesies = "Kucing"

    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

    def run(self,speed):
        print(f"Kucing {self.nama} berlari dengan {speed}...")

    def play(self):
        print(f"Kucing {self.nama} bermain dengan kucing lainnya...")   

    def eat(self):
        pass 

# Membuat objek
kinako = Cat(nama="Kinako", tipe="Anggora")
minto  = Cat(nama="Minto", tipe="Persia")

print(f"Kinako adalah seekor {kinako.__class__.spesies}")
print(f"{kinako.nama} merupakan kucing jenis {kinako.tipe}")
print(f"{minto.nama} merupakan kucing jenis {minto.tipe}")

# print(kinako)
# print(minto)

kinako.run(speed='cepat')
kinako.play

print(kinako.__doc__)

del kinako.tipe

print(kinako.tipe)

class Employee():
    """
    Ini adalah class untuk memanipulasi data employee
    Melalui kelas ini kita bisa memaipulasi data yang ada seperti baca, hapus dan tambah
    """

    def __init__(self, lokasi_file):
        self.data_employee = open(f'{lokasi_file}', mode='r', encoding='utf-8')
        self.data_per_sesi = 10
    
    def baca_data(self):
        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee
    
    def hapus_data(self, baris, kolom):
        del self.data_employee[baris][kolom]
    
    def tambah_data(self, data_baru):
        nama, gaji, posisi, jabatan, domisili = data_baru
        self.data_employee.append([nama, gaji, posisi, jataban, domisili])

#membuat objek
it = Employee(lokasi_file='./karyawan_IT.xls')
marketing =  Employee(lokasi_file='./karyawan_marketing.xls')
product = Employee(lokasi_file='./karyawan_product.xls')

# ABSTRACT OBJEK
class RandomForest():
    pass

# LATIHAN
# Buatlah satu class Mobil yang bisa digunakan untuk mencetak beragam tipe mobil
# Pastikan class tersebut memiliki setidaknya 3 attributes dan 3 methods

class Mobil:
    def __init__(self, nama, type, color):
                self.nama = nama
                self.tipe = type
                self.color = color
    
    def start(self, speed):
        pass
    def stop(self):
        pass
    def brake(self):
        pass        