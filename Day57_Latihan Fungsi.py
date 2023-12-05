'''Latihan Fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# Membuat header program
os.system("cls")

print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
print(f"{'-':^40}")

# Mengambil input user
LEBAR = int(input("Masukkan nilai lebar: "))
PANJANG = int(input("Masukkan nilai panjang: "))

# program menghitung luas
LUAS = PANJANG*LEBAR
KELILING = 2*(PANJANG*LEBAR)

# tampilkan hasilnya
print(f"hasil perhitungan luas = {LUAS}")
print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''Fungsi Header'''
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-':^40}")

def input_user():
    '''fungsi Header'''
    # Mengambil input user
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return  2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")


# program utamanya
while True:
    header( )
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display(f"luas",LUAS)
    display(f"keliling",KELILING)

    isContinu = input("apakah lanjut (y/n)? ")
    if isContinu == "n":
        break

print("Program selesai, terima kasih")