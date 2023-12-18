# Contoh 4
nilai = 0
nama = "Gunung"

def perbarui(nilai_baru, nama_baru):
    global nilai  # Fungsi ini dapat mengubah nilai
    global nama
    nilai = nilai_baru
    nama = nama_baru

print(f"Sebelum perubahan: {nilai, nama}")
perbarui(8, "Laut")
print(f"Sesudah perubahan: {nilai, nama}")

# Contoh 5
nilai = 0

for j in range(0, 5):
    nilai += j
    nilai_dummy = 0

print(f"Total nilai: {nilai}")
# print(nilai_dummy)  # Komentari baris ini agar tidak terjadi NameError

if True:
    nilai = 15
    nilai_dummy = 15

print(f"Nilai setelah kondisi: {nilai}")
print(f"Nilai dummy setelah kondisi: {nilai_dummy}")