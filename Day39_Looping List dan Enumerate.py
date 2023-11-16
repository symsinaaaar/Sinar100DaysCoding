# looping dari list

# for loop
print("For loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Sinar", "Juli", "Mentari", "Flo"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nFor loop dan range")
kumpulan_angka =[10,5,4,2,6,5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print("\n While loop")
kumpulan_angka =[10,5,4,2,6,5]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("\nList Comprehension")
data = ["Sinar",1,2,3,"Juli"]
[print(f"data ={i}") for i in data]

angka =[10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nEnumerate")
data_list= ["Sinar",1,2,3,"Juli"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")