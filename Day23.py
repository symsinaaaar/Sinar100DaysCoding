# soal hari ini (Percabangan)
# buatkan sebuah program yang menginputkan nama, penghasilan bulanan, pekerjaan
# memiliki kondisi Ketika penghasilan perbulan lebih dari 3jt maka mendapat pajak 5%
# jika penghasilan lebih dari 10jt maka mendapat pajak 15%
# lalu Ketika pekerjaan beliau adalah petani maka akan mendapatkan bantuan dana sebesar 1.000.000 perbulan
# Jika pekerjaan PNS maka tidak mendapatkan apapun
# jika selain petani dan selain PNS maka mendapatkan bantuan sebesar 200.000
# lalu hitung total gaji bersih perbulannya

nama = input("Masukkan nama Anda: ")
pekerjaan = input("Masukkan pekerjaan Anda: ")
penghasilan_bulanan = int(input("Masukkan penghasilan bulanan Anda: "))

pajak = 0
bantuan = 0
gaji_sementara = 0
gaji_bersih = 0

if penghasilan_bulanan > 3000000:
    pajak = penghasilan_bulanan * 0.05
elif penghasilan_bulanan > 10000000:
    pajak = penghasilan_bulanan * 0.15
else:
    pajak = 0

gaji_sementara = penghasilan_bulanan  - pajak

if pekerjaan == "Petani":
    bantuan = 1000000
elif pekerjaan == "PNS":
    bantuan = 0
else:
    bantuan = 200000
    
gaji_bersih = gaji_sementara + bantuan
print("gaji_bersih", gaji_bersih)