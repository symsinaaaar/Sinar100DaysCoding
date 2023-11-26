import datetime
import os

# template dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks':0,
    'lahir':datetime.datetime(2003,8,13)
}

data_mahasiswa = {}

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
mahasiswa['Lahir'] = datetime.datetime(Tahun_Lahir, Bulan_Lahir, Tahun_Lahir)
print(mahasiswa)