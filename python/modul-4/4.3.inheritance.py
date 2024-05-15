# KONSEP INHERITANCE
# Inheritance adalah konsep pada OOP yang memungkinkan kita untuk mendefinisikan kelas yang mewariskan semua fungsionalitas dari kelas induk (parent) dan memungkinkan kita untuk menambahkan lebih banyak lagi.

# Apa itu inheritance?
# inheritance merupakan fitur yang penting dalam OOP.

# Dengan inheritance, kita bisa mendefinisikan kelas baru hanya dengan sedikit modifikasi dari kelas yang sudah ada. kelas baru disebut kelas child da kelas yang diwarisinya disebut kelas parent atau base.

# menerapkan inheritance pada OOP
# class ParentClass:
    # isi dari parent class

# class ChildClass(ParentClass):
    # isi dari child class

# contohnya inheritance
# class Animal:
#     def __init_(self):
#         self.tipe = "Mamalia"
    
#     def grow(self):
#         print("Mamalia ini bertumbuh...")

# class Cat(Animal):
#     def __init_(self):
#         self.nama = "Meong"
#         self.tipe = "Anggora"
    
#     def run(self):
#         print("kucing berlari")

# Overriding
# tujuan kita mewarikan semua fungsionalitas dari kelas induk (parent) ke kelas baru (child) adalah agar fungsionalitas yang sudah ada bisa dikembangkan atau dikenal dengan istilah overriding. lalu bagaimana fungsi __init__() yang ada pada keduanya?

# gunakan ini pada kelas baru super().__init__('Nama Kelas')

# Kesimpulan:
# inheritance adalah konsep pada OOP untuk mendefinisikan kelas yang mewarikan semua fungsionalitas

# pewarisan fungsionalitas agar bisa dikembangkan dikenal juga dengan istilah ovverriding

# pada akhirnya ini mendukung ide tentang reusability pada kode-kode yang telah dibuat

# Praktik
# PARENT CLASS
class Animal:
    def __init__(self):
        self.tipe = "Mamalia"
        self.kecepatan = "Lambat"
    
    def grow(self):
        print("Mamalia ini bertumbuh...")

# CHILD CLASS
class Cat(Animal):
    def __init__(self, nama, tipe):

        super().__init__()

        self.nama = nama
        self.tipe = tipe
    
    def run(self):
        print(f"kucing {self.tipe} berlari...")

class Dog(Animal):
        pass

kinako = Cat(nama="Kinako", tipe="Anggora")
minto = Cat(nama="Minto", tipe="persia")

print(kinako.kecepatan)
print(kinako.tipe)

kinako.run()
minto.run()

kinako.grow()
minto.grow()

#LATIHAN
# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki parent class bernama Kendaraan
# Pastikan parent class tersebut memiliki setidaknya 2 attributes dan 2 methods yang akan diturunkan ke child class
# Jangan lupa menggunakan super() pada child class

# Parent class
class Kendaraan:
    def __init__(self, jenis, merk):
        self.jenis = jenis
        self.merk = merk

    def nyalakan_mesin(self):
        print(f"Mesin {self.jenis} {self.merk} dinyalakan.")

    def matikan_mesin(self):
        print(f"Mesin {self.jenis} {self.merk} dimatikan.")

# Child class
class Mobil(Kendaraan):
    def __init__(self, merk, jumlah_pintu):
        super().__init__('Mobil', merk)
        self.jumlah_pintu = jumlah_pintu

    def buka_pintu(self):
        print(f"Membuka {self.jumlah_pintu} pintu dari {self.merk}.")

    def tutup_pintu(self):
        print(f"Menutup {self.jumlah_pintu} pintu dari {self.merk}.")

# Contoh penggunaan
mobil_saya = Mobil('Toyota', 4)
mobil_saya.nyalakan_mesin()
mobil_saya.buka_pintu()
mobil_saya.tutup_pintu()
mobil_saya.matikan_mesin()