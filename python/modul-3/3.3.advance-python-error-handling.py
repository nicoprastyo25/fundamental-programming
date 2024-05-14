# KONSEP ERROR HANDLING

# Apa itu ERROR HANDLING
# pada saat melakukan programming, kita dapat membuat kesalahan tertentu saat menulis program yang menyebabkan error dan ini perlu ditangani. program python berakhir segera ketika menemukan kesalahan yang tidak ditertangani

# 2 tipe error
# Error pada bahasa pemrograman secara umum bisa dibagi menjadi 2 yaitu:
# 1. Syntax error
# 2. Logical Error

# Syntax error
# Contoh
# ini adalah contoh error
#fruit_list = ['apple','banana']
# for fruit in fruit_list
# SyntaxError: invalid syntax
# kesalahan jika pada syntax ada yang lupa tanda petik, kurung kurawal,dll
# syntax error mudah ditangani

# Logical Error
# Contoh penerapan
# ini adalah contoh error
# nilai = 10
# pembagi = 0
# hasil = nilai/pembagi
# ZeroDivisionError: division by zero
# kesalahan jika logikal
# syntax error mudah ditangani

# Exception
# Exception merupakan keadaan dimana saat kode tidak ada kesalahan secara sintaks tapi muncul error lainnya

# beberapa contoh dari exception yang dimiliki oleh python adalah
# - ZeroDivisionError 
# - ValueError
# - AttributeError
# - ImportError
# - IndexError

# Error handling with try except
# kita dapat mengatur agar program kita aagar tidak menghasilkan pesan error yang tidak disengaja dan kita dapat melakukan pengecekan pada tempat yang kita inginkan dengan try-except
# Error handling with try except
# contoh
# Try:
#   serangakaian_kode_kita (loop, fungsi, dll)
# Except:
#   kode_alternatif_atau_pernyataan_jika_kode_gagal_dijalankan

# LOGICAL ERROR
# error semacam ini, bahkan bisa tampak seperti baik0baik saja, tidak ada informasi error, namun logika pemrograman tidak bekerja seabgaimana mestinya, misal a+b semestinya menghasilkan 10(int)

#Kesimpulan
# pada saat melakukan programming, kita dapat membuat kesalhan tertentu saat menulis program yang menyebabkan error
# error pada bahasa pemrograman secara umum bisa dibagi menjadi 2 yaitu syntax error dan logical error
# try-except bisa dilakukan untuk error handling

#Praktek
# syntax error
# fruit_list = ['apple','banana']
# for fruit in fruit_list
#     print fruit

# SyntaxError: expected ':'

# LOGICAL Error
nilai = 10
pembagi = 0
# hasil = nilai/pembagi

print ("instruksi setelahnya")

# print(dir(locals()['__builtins__'])) #melihat kategori error pada python
# ZeroDivisionError: division by zero

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except:
    print ("instruksi alternatif untuk melanjutkan kode")

#BEST PRACTICES
try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except Exception as e:
    print ("instruksi alternatif untuk melanjutkan kode", e.__class__,".")

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except ZeroDivisionError:
    print ("Ooops! terjadi Zerodivision error")
except ValueError:
    print ("Ooops! terjadi Value Error")
except :
    print ("Error tidak ditemukan")

# Membuat error handling sendiri
class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

number = 10
while True:

    try:
        i_num = int(input("Masukan angka: "))

        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Angka yang kamu tebak terlalu kecil, coba lagi!")
        print()
    except ValueTooLargeError:
        print("Angka yang kamu tebak terlalu besar, coba lagi!")
        print()

print("Betul! kamu berhasil menabak dengan tepat.")

#Latihan
# Instruksi cetak di bawah menyebabkan program terhenti karena mengalami IndexError
# Tangani error tersebut dengan teknik Error Handling yang sudah dipelajari
# Setelah itu, jalankan program dan pastikan tidak ada lagi pemberitahuan error pada program

list = [1, 3, 5, 7, 9, 11, 13, 15]

try:
    print(list[20])
except IndexError:
    print("Ops terjadi error pada index Error")
