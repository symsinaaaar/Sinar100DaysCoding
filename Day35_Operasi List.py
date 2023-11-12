### Operasi List ###
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data_angka = \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
print(f"jumlah data 4 = {jumlah_data_4}")
jumlah_data_3 = data_angka.count(3)
print(f"jumlah data 4 = {jumlah_data_3}")

# ambil posisi data
data = ["Sinar", "Juli", "Mentari", "Flo"]
print(f"data = {data}")

index_Mentari = data.index("Mentari")
print(f"index si Mentari = {index_Mentari}")

index_Flo = data.index("Flo")
print(f"index si Flo = {index_Flo}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")