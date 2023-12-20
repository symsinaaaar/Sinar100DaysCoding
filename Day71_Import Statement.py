# import <- berfungsi untuk mengambil program dari file external .py

# 1. untuk menyambung program dari external
import program_print
import program_sinar

# 2. import dengan data
import variabel
import Juli

# data ada di namespace variabel
print(variabel.data)
print(Juli.data)

# 3. import dengan fungsi
import matematiaka

hasil = matematiaka.tambah(4,5)
print(hasil)