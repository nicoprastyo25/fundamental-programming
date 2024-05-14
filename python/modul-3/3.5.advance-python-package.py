# KONSEP PACKAGE

# apa itu package?
# package pada dasarnya memiliki tujuan yang sama seperti modul, yaitu agar program python yang kita miliki bersifat manageable dan reousable. memastikan bahwa sekumpulan file yang ada memiliki hirarki yang baik

# seiring program bertumbuh. kita menempatkan kode-kode yang serupa pada satu modul, dan modul-modul yang serupa pada satu package. sederhananya, modul itu sama dengan file, sedangkan package sama dengan folder.

# Jika aplikasi pemutar lagu semakin besar, sebaiknya modul singer.py menjadi package singer.py menjadi package singer yang memuat didalamnya modul-modul profile.py dan album.py

# music->package
#     - _init_.py
#     - playlist -> package
#         -_init_.py
#         -play.py
#         -pause.py
#         -load.py
#     - singer  -> package
#         -_init_.py
#         -profile.py
#         -album.py
#     - music -> package
#         -_init_.py
#         -genre.py
#         -desc.py

# menggunakan package di python
# contoh penerapan
# ini adalah file main.py yang menggunakan package playlist
# import Music.Playlist.play as Play
# Play.play("digimon - butterfly")

# Kesimpulan
# sekumpulan module dan package yang terorganisir dengan baik disebut sebagai library yang bisa di-install melalui PIP seperti Numpy, Pandas, Matplotlib dan Seaborn.

#package meiliki konsep yang sama seperti modul dan digunakan seiring program yang terus bertumbuh
# sederhananya, modul itu sama dengan file, sedangkan package sama dengan folder

# Praktik
import Music.Playlist.play as Play
import Music.Playlist.pause as Pause
import Music.Playlist.load as Load

Play.play("Digimon - Butterfly")
Pause.pause("Naruto - Flow")
Load.load("Paterpan - Bintang disurga")

# Latihan
# Kembangkanlah modul game yang sudah dibuat sebelumnya menjadi package
# Package tersebut berupa folder yang memuat modul-modul terkait Hero, Item, Enemy, Area dan Rank
# Lalu import package game tersebut ke satu file python bernama main.py
import Game.area as Area
import Game.enemy as Enemy
import Game.hero as Hero
import Game.item as Item
import Game.rank as Rank

Area.area("Ranked")
Enemy.enemy("Franco")
Hero.hero("Kadita")
Item.item("Sepatu magic")
Rank.rank("Mytical Glory")