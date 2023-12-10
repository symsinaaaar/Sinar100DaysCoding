# lambda function

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# menggunakan lambda
# output = lambda argument: expression
kuadrat = lambda angka:angka**2
print(f"hasil lambda kuadrat = {kuadrat(3)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

## kegunaan
# sorting untuk list biasa

data_list = ["Sinar", "Juli", "Mentari"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

# sort pakai lambda
data_list = ["Sinar", "Juli", "Mentari"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<5,data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3
data_kelipatan_3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_kelipatan_3)