data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1]
print(f"list 2d = {list_2D}")

list_2D = [data_0, data_1, data_list_biasa]
print(f"list 2d = {list_2D}")

list_2D = [data_0, data_1, 6, 7]
print(f"list 2d = {list_2D}")

# contoh penggunaan
peserta_0 = ["Sinar", 20, "Perempuan"]
peserta_1 = ["Juli", 20, "Perempuan"]
peserta_2 = ["Indra", 21, "Laki-laki"]

list_peserta = [peserta_0, peserta_1, peserta_0]
print(f"peserta = {list_peserta}")
for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")

# dengan reference
list_copy = list_peserta.copy();
print(f"peserta = {list_copy}")
peserta_0 [0] = "Mentari"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")