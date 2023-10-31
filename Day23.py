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
    bantuan = 200
    
gaji_bersih = gaji_sementara + bantuan
print("gaji_bersih", gaji_bersih)