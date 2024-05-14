# KONSEP FILE HANDLING

# apa itu file handling
# python memiliki beberapa fungsi untuk mengelola file seperti membuat, membaca, memperbaharui, dan menghapus file.
# dengan fungsi ini, python bisa menangani normal file seperti teks ataupun binary file (0s dan 1s)

# Apa itu file handling?
# ada 3 jenis metode operasi dasar di python yaitu
# -----------------------------------------------------
# |   Mode    |    Makna      |       Deskripsi       |
# -----------------------------------------------------
# |    r      |   Read        |  untuk membaca file   |
# -----------------------------------------------------
# |    a      |   Append      | untuk menambah data   |
# -----------------------------------------------------
# |    w      |   Write       | Untuk menulis data    |
# -----------------------------------------------------

# Operasi Read
# Contoh penerapan
# ini adalah instruksi untuk membaca file txt
data = open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='r')
data = open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='r', encoding='utf-8') #Rekomended menggunakan encoding

print(data.read()) #Latihan dasar menangani file di python
string = data.read()
string = string.replace("adalah", "merupakan")
print(string)

# Operasi Append
# Contoh penerapan
# ini adalah instruksi untuk menambah data file txt
data = open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='a')
data.write("\n Yuk belajar bahasa pemrograman python!")
data.write("\nAgar jago harus sering berlatih!")
data.close() #digunakan untuk menghapus memori yang sudah tidak digunakan lagi


# Operasi Write
# Contoh penerapan
# ini adalah instruksi untuk mengubah data file txt
data = open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='w')
data.write("\n Yuk belajar bahasa pemrograman python!")
data.write("\nAgar jago harus sering berlatih!!")
data.close() #digunakan untuk menghapus memori yang sudah tidak digunakan lagi

#Kesimpulan
# File handling adalah fungsi khusus dalam bahasa pemrograman python untuk mengelola file
# dengan fungsi ini, python bisa menangani normal file seperti teks ataupun binary file (0s dan 1s)
# ada 3 jenis metode operasi dasar di python yaitu Read(), Append(), Write()

# Praktik
# Better practice
try:
    f =  open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='w', encoding='utf-8')
finally:
    f.close()

#pisahkan proses operasi kita dengan close, selama ngoding apapun jika ada error akan tetap nutup prosesnya

# Best Practice
# with open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='w', encoding='utf-8') as f:
#     f.read()
#     f.write()

# Latihan
# Bacalah data yang ada di file data.txt
# Lalu tambahkan teks "Bahasa Pemrograman Python memiliki masa depan yang cerah"
# Pastikan tidak menghilangkan data yang sudah ada di file tersebut!
data = open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='r', encoding='utf-8')
data = open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='w', encoding='utf-8')
data.write("Bahasa Pemrograman Python memiliki masa depan yang cerah")
data.close()
data = open('C:/Users/PTP2/Documents/programming/python/modul-3/data.txt', mode='r', encoding='utf-8')