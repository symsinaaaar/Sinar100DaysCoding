## Operasi

# index  0(-3)    1(-2)     2(-1)
data = ["Sinar", "Juli", "Mentari"]

# mengambil data dari list ini

data_index_0 = data[0]
print(f"data pertama (index 0) = {data_index_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_Sinar = data[-3]
print(f"data_Sinar = {data_Sinar}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebwelum di tambahkan = \n{data}")

# data.insert(posisi, item) <- cara manipulasi sesuai posisi
data.insert(1,"Lala")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Kumala")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["Pipi", "Wiwi", "Boboy"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data kedua
data[2] = "Flo"
print(f"data setelah di ubah = \n{data}")

# meremove data
data.remove("Lala")
print(f"data remove = \m{data}")

# meremove data paling belakang
data.pop()
print(f"data akhir = \n{data}")