import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks':0,
    'lahir':datetime.datetime(2003,8,13)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("_"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa ['nama']= input("Nama Mahasiswa: ")
    mahasiswa ['nim']= input("NIM Mahasiswa: ")
    mahasiswa ['SKS']= int(input("Jumlah SKS: "))
    Tahun_Lahir = int(input("Tahun Lahir(YYYY): "))
    Bulan_Lahir = int(input("Bulan Lahir(1-12): "))
    Tanggal_Lahir = int(input("Tanggal Lahir(1-31): "))
    mahasiswa['Lahir'] = datetime.datetime(Tahun_Lahir, Bulan_Lahir, Tanggal_Lahir)
   
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (6)))
    data_mahasiswa.update({'KEY':mahasiswa})

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM:<8'} {'SKS':<5} {'Lahir':<15}")
    print("_"*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{'KEY':<6} {'NAMA':<17} {'NIM:<10'} {'SKS':<5} {'LAHIR':<15}")
        print(f"{'KEY':<6} {'NAMA':<17} {'NIM:<10'} {'SKS':<5}  {'LAHIR':<15}")

        print("\n")
        is_done = input("Sudah selesai (y/n)?")
        if is_done == "n":
            break
        print("\nAkhir dari program")