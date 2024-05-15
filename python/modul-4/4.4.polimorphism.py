# POLIMORPHISM
# apa itu polimorphism
# polimorfisme adalah kemampuan dalam OOP untuk menggunakan satu fungsi umum untuk kemudian bekerja secara beragam tergantung object yang diberikan

# Menerapkan Polimorphism pada OOP
# class Cat:
#     def __init__(self):
#         self.nama = "Meong"
#         self.tipe = "Anggora"
    
#     def forward(self):
#         print("Kucing berlari")

# class Bird:
#     def __init__(self):
#         self.nama = "Erago"
#         self.tipe = "Elang"
    
#     def forward(self):
#         print("Burung Terbang")

# # Menerapkan polimorphism pada OOP

#     def melaju(objek):
#         objek.forward()
    
# meong = Cat()
# erago = Bird()

# melaju(meong)
# melaju(erago)

    # KESIMPULAN
    # polimorfism adalah konsep pada OOP untuk kita memungkinkan melakukan keberagaman jalannya satu fungsi umum

    # konsep ini biasanya dimanfaatkan ketika kode-kode pemrograman semakin rumit sehingga paradigma objek dengan konsep seperti encapsulation, inheritance, dan polimorphism sangat membantu

# Praktik
class Cat:
    def __init__(self):
        self.nama = "Meong"
        self.tipe = "Anggora"
    
    def forward(self):
        print("Kucing berlari")

class Bird:
    def __init__(self):
        self.nama = "Erago"
        self.tipe = "Elang"
    
    def forward(self):
        print("Burung Terbang")

# Menerapkan polimorphism pada OOP

def melaju(objek):
    objek.forward()
    
meong = Cat(); erago = Bird()

melaju(meong)
melaju(erago)
