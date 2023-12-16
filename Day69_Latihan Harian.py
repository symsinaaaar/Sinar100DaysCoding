def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error! Tidak dapat membagi oleh nol."
    else:
        return a / b

print("Pilih operasi:")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print(angka1, "+", angka2, "=", tambah(angka1, angka2))
elif pilihan == '2':
    print(angka1, "-", angka2, "=", kurang(angka1, angka2))
elif pilihan == '3':
    print(angka1, "*", angka2, "=", kali(angka1, angka2))
elif pilihan == '4':
    print(angka1, "/", angka2, "=", bagi(angka1, angka2))
else:
    print("Input salah")