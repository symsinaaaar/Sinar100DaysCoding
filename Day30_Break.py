# Break
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    
    if angka == 3:
        print("Nice!")
        break
    print("Wawwww!")
print("Finish!!!")

data_int = int(input("Hitung samapai = "))
angka = 0
while True:
    angka += 1
    print(f"count = {angka}")
    
    if angka == data_int:
        print("Nice!")
        break
    print("Wawwww!")
print("Finish!!!")