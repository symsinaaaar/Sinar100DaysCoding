# Continue and Pass

# Pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        print("wawwww")

    print(angka)
print("akhir dari program \n")

angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass # ini tidak akan dieksekusi

    print(angka)
print("akhir dari program \n")

# Continue
angka = 0
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    print("wawww")
print("Nice!")

angka = 0
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1
    if angka == 3:
        print("Nice!")
        continue # akan membuat loop meloncat ke step selanjutnya
    print("wawww") # aksi 2
print("Finish!")