# Program penentu menu makanan acak

import random

# Fungsi untuk memilih menu makanan acak
def pilih_menu_acak():
    menu_makanan = ["Nasi Goreng", "Pizza", "Sushi", "Burger", "Mie Ayam"]
    return random.choice(menu_makanan)

# Cetak menu makanan acak untuk hari ini
print("Menu makanan untuk hari ini:", pilih_menu_acak())