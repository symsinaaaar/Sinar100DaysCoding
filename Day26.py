# for loop (Perulangan)

angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

# for kondisi:
# aksi

# ini dengan list
angka2_list = [0, 1, 2, 3, 4] # ini adalah list
print(angka2_list)

for i in angka2_list:
    print(f"i sekarang -> {i}")
print("akhir dari program \n")

angka2 = [0, 2, 4, 8, 10] # ini adalah list
print(angka2)

for i in angka2:
    print(f"i sekarang -> {i}")
print("akhir dari program \n")

# ini dengan range
angka2_range = range(5)
for i in angka2_range:
    print(f"i sekarang -> {i}")
print("akhir dari program \n")

angka2_range = range(1,10)
for i in angka2_range:
    print(f"i sekarang -> {i}")
print("akhir dari program \n")

# menggunakan string
data_str = "saya keren banget"
for huruf in data_str:
    print(huruf)
print("akhir dari program")