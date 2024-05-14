# KONSEP Regex
# RegEx atau Regular Expression adalah satu fungsi khusus untuk mendefinisikan pola tertentu melalui serangkaian karakter yang kemudian dioleh bahasa pemrograman. di python. fungsi ini bisa digunakan melalui modul khusus bernama re.

# Apa itu Regex
# contoh serangkaian karakter untuk mendefinisikan pola tertntu yang ada pada RegEx,

# ^s...t$

# yang berarti: apapu kata yang terdiri 5 karakter dimulai dari karakter s da di akhiri oleh karakter t

# short(match)
# skin
# smart(match)
# she is smart
# shampoo

# Menggunakan RegEx di python
# Contoh penerapan
#ini adalah contoh penerapan regex pada python
import re

pattern = '^s...t$'
result = re.match(pattern,'smart')#ouput True
print(result)

# fungsi pada RegEx di python
# ada banyak fungsi yang disediakan oleh RegEx seperti match(),findall(),search(),split(),sub() dan sebagainya

# fungsi
# match() = mengembalikan status kecocokan
# findall() = mengembalikan list yang memuat semua string yang cocok
# search() = mengembalikan status kecocokan dimanapun yang ada pada SyntaxWarning
# split() = mengembalikan list dari string yang telah di-split berdasarkan kecocokannya
# sub() = mengubah bagian dari string berdasarkan kecocokan

# Karakter-deskripsi-contoh
# [] -> Sekumpulan karakter          -> "[a-m]"
# \  -> menggunakan spesial karakter -> "\d"
# .  -> karakter apapun              -> "he..o"
# ^  -> dimulai dengan               -> "^hello"
# $  -> diakhiri dengan              -> "planet$"
# *  -> 0 atau lebih keberadaan      -> "he.*o"
# +  -> satu atau lebih keberadaan   -> "he.+o"
# ?  -> 0 atau 1 keberadaan          -> "he.{2}o"
# |  -> atau                         -> "falls|stays"
# \d -> String memuat digits (0-9)
# \D -> String tidak memuat digits (0-9)
# \s -> String memuat spasi
# \S -> String tidak memuat spasi
# \w -> String memuat karakter apapun
# \W -> String tidak memuat karakter apapun

# KESIMPULAN
# RegEx atau Regular Expression adalah satu fungsi khusus untuk mendefinisikan pola tertentu melalui serangkaian karakter
# Biasanya modul ini bermanfaat untuk kita memproses atau mengelola data dalam bentuk teks secara efektif

# Praktik

import re

teks = "regex"
x = re.match("^r...x$", teks)
print(x)

teks = "saya senang belajar regex"
x = re.split("\s", teks)
print(x)

teks = """
    Ada 3 tipe loop atau perulangan di bahasa pemrograman python yaitu while loop
    for loop dan nested loop 2022
"""
x = re.sub("\d+", "", teks)
print(x)

teks = "Hujan deras di kawasan depok"
result = re.search("^Hujan.*depok$", teks)

if result:
    print("Yes! we have a match.")
else:
    print("No match.")

teks = "23 oct 2019 23 oct,2019 23 october,2019 oct 26,2020"
x = re.findall("\d{2} [a-z]{3} \d{4}",teks)
print(x)

teks = "Harga 1 modul antik tersebut yaitu $1000"
# sensor harga
x = re.sub("\$\d+", "-", teks)
print(x)

teks = "akan dialihkan ke http://medium.com"
x =re.sub("http[s]?://\S+","_",teks)
print(x)

teks = "Luas biasa! banyak anak-anak muda traveling tahun ini, begini tanggapan lesti #travel #_lesti #viral #gadget"
x = re.findall("#[_]*[a-z]+", teks)
print(x)

# Latihan
# Coba tangkap informasi domisili (Tokyo) dan informasi nomor (021 7581 6521) pada 2 teks berikut
# Gunakan modul regex (re)

teks1 = "Saya yang berdomisili di Tokyo bisa dihubungi di nomor berikut 021 7581 6521"
x = re.findall("Tokyo",teks1)
print(x)

teks2 = "Nomor ini tidak bisa dihubungi 021 1121 6551, karena sudah di luar area Tokyo"
x = re.search("r'\b\d{3}\s\d{4}\s\d{4}\b'", teks)
print(x)
