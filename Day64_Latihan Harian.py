# Program Menentukan Bilangan Genap atau Ganjil

# Fungsi lambda untuk menentukan bilangan genap atau ganjil
cek_genap_ganjil = lambda angka: "Genap" if angka % 2 == 0 else "Ganjil"

# Input dari pengguna
bilangan = int(input("Masukkan bilangan: "))

# Menggunakan lambda function untuk menentukan genap atau ganjil
hasil_cek = cek_genap_ganjil(bilangan)

# Tampilkan hasil
print(f"Bilangan {bilangan} adalah {hasil_cek}")