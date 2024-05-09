# Konsep
# Operator adalah simbol khusus yang digunakan untuk melakukan operasi matematika dasar yang bertujuan untuk membuat sebuah alur logika pada bahasa pemrograman

# python memiliki 2 operator dasar yaitu Operator aritmatika dan operator perbandingan


# Operator aritmatika merupakan operator dasar yang terdiri dari operasi operasi matematika dasar

'''
Operator    Nama            Contoh
    +       Penjumlahan     x + y
    -       Pengurangan     x - y
    *       Perkalian       x * y
    /       Pembagian       x / y
    %       Modulus         x % y       # Menghasilkan sisa bagi contoh 5%2=1 6%3=0 7%3=1
    ^       Exsponesial     x ** y      # Pangkat
'''

# Operator perbandingan merupakan operator yang digunakan untuk membandingkan sebuah nilai atau variabel dengan operan tertentu

'''
Operator        Nama                                Contoh
==              sama dengan                         x == y
!=              Tidak sama dengan                   x != y
>               Lebih Besar                         x > y
>=              Lebih Besar atau sama dengan        x >= y
<               Lebih Kecil                         x < y
<=              Lebih Kecil atau sama dengan        x <= y
'''

# Operator Aritmatika
print (13 + 12 ) #output 25
a = 10
b = 1
print(a - b) #Output 9

# Operator Perbandingan
print (13 == 12) #Output False
a = 10
b = 1
print(a > b) # Output True

# Kesimpulan
# - Operator adalah simbol khusus untuk membuat sebuah alur logika
# - Pada python terdapat dua operator dasar yaitu Operator Aritmatika dan Operator Perbandingan
# - operasi aritmatika merupakan operasi matematika dasar sedangkan operator perbandingan adalah membandingkan suatu nilai dengan nilai lainnya

# Praktik
a = 5
b = 3
print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a % b)
print(a ** b)

a = 5
a += 3 #variable_saya  = variable_saya + 3
print(a)

s = "ini adalah string "
print(s * 3)

s = "*"
print(s * 3)

b = True #True = 1 False=0
print(b/2)

#Operator Perbandingan
x = 10
y = 15

print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

print(x is y) # is berarti sama dengan
print(x is not y) # is not berarti tidak sama dengan