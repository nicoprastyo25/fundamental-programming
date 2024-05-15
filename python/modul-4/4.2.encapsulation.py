# KONSEP ENCAPSULATION
# apa itu encapsulation (pengkapsulan)
# dengan menggunakan OOP di python, class bisa membatasi akses ke atribut dan metode. ini mencegah data dari modifikasi langsung atau dari perubahan tidak disengaja, dan ini disebut dengan enkapsulasi

# dalam python, untuk menandai atribut-atribut privat kita bisa menggunakan tanda underscore sebagai prefix single (_) ataupun double (__)

# menerapkan Encapsulation pada OOP
# class Mobil:
#     def __init__(self):
#         self.__tipe = "Avanza"
#         self.__bensin = "40" #Liter

# Setter & Getter
# dengan enkapsulasi, atribut dan metode pada class yang kita definisikan akan bersifat terbatas dalam hal akses, namum bisa tetap diubah melalui fungsi setter & getter yang dibuat. biasanya diberi nama method set() dan get() atau atur() dan lihat()

# class Mobil:
#     def __init__(self):
#         self.__tipe = "Avanza"
#         self.__bensin = "40" #Liter
    
#     def aturMaksimumBensi(self,bensin):
#         self.__bensin = bensin

# KESIMPULAN
# Dengan konsep enkapsulasi, class membatas akses ke atribut dan metode pada satu kelas tertentu

# Atribut dan metode tidak akan pernah bisa diubah dari luar kelas kecuali disediakan fungsi setter dan getter

# PRAKTIK
class Mobil:
    def __init__(self, plat):
        # sebelum menggunakan encapsulation
        # self.plat = plat
        # self.tipe = "Avanza"
        # self.bensin = "40" #Liter

        self.__plat = plat
        self.__tipe = "Avanza"
        self.__bensin = "40" #Liter
    
# getter
    def lihatMaksimumBensin(self):
        print(f"Maksimum bensin yaitu: {self.__bensin} liter")
# setter
    def aturMaksumumbensin(self, bensin):
        self.__bensin = bensin

avanza = Mobil(plat="B 7185")
# print(avanza.plat)
# print(avanza.tipe)
# print(avanza.bensin)

avanza.__bensin = 30
print(avanza.__bensin)

avanza.lihatMaksimumBensin()
avanza.aturMaksumumbensin(bensin=100)

# LATIHAN
class Mobil:
    def __init__(self, plat, tipe, bensin):
        self.__plat = plat
        self.__tipe = "Avanza"
        self.__bensin = "40" #Liter

    # Tambahkan setter & getter
    # getter
    def lihatMaksimumBensin(self):
        print(f"Maksimum bensin yaitu: {self.__bensin} liter")
    # setter    
    def aturMaksumumbensin(self, bensin):
        self.__bensin = bensin

avanza.lihatMaksimumBensin()
avanza.aturMaksumumbensin(bensin=100)