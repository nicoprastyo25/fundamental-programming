# KONSEP MODULE
# Module merujuk pada file python yang memuat kode-kode pemrograman (statement) terpisah dari file python utama semisal kode.py. disebut sebagai sebuah modul yang bernama kode block.py disebut juga sebagai modul yang bernama block

# Apa itu module?
# konsep modul digunakan ketika ingin memecah satu file python besar menjadi bagian yang lebih kecil.sehingga file-file python yang kita miliki lebih manageable dan reusable

# Misalnya kita ingin membuat aplikasi pemutar lagu, maka akan lebih baik jika program python kita dipecah menjadi bagian-bagian kecil seperti playlist.py, singer.py, music.py dan sebagainya

# membuat module di python
# contoh penerapan
# ini adalah file playlist.py yang memuat fungsi play
# def play(song):
#     print("Memutar lagu berjudul " + song)

#ini adalah file main.py yang menggunakan module playlist.py
# import playlist

# playlist.play("Digimon - Butterfly")

# Built-In Module
# python memiliki modul-modul bawaan yang bisa kita manfaatkan untuk kebutuhan spesifik seperti modul math, os dan juga module re.

# Kesimpulan
# - konsep modul digunakan ketika kita ingin memecah satu file python besar menjadi bagian yang lebih kecil
# - dengan modul, maka file-file python yang memiliki lebih manageable dan reusable
# - kita bisa membuat modul kita sendiri atau menggunakan modul bawaan dari python seperti math, os ataupun re

# Praktek

# Praktek
import playlist

playlist.play('Digimon - Butterfly')
playlist.pause('Digimon - Butterfly')

import playlist as pl #REKOMENDED

pl.play('Digimon - Butterfly')
pl.pause('Digimon - Butterfly')
print(pl.GENRE)


from playlist import GENRE,DURATION, TYPE
print(GENRE)
print(DURATION)
print(TYPE)

from playlist import *
print(GENRE)
print(DURATION)
print(TYPE)
play("digimon - butterfly")

import os
import math

from math import pi
from math import e

print(pi)
print(e)

print(os.cpu_count())