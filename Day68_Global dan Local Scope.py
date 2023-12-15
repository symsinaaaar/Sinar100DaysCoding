## contoh 2
angka = 0
name = "Sinar"

def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka, name}")
ubah(10,"Mentari")
print(f"Sesudah {angka, name}")

## contoh 3
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)