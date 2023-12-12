# Program Kalkulator Luas Persegi atau Persegi Panjang

# Fungsi lambda untuk menghitung luas
hitung_luas = lambda panjang, lebar: panjang * lebar

# Input dari pengguna
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

# Hitung luas menggunakan lambda function
luas = hitung_luas(panjang, lebar)

# Tampilkan hasil
print(f"Luas persegi atau persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")