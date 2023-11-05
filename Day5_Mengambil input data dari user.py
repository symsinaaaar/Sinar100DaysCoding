##Mengambil input data dari user
# Mengambil data str
data = input ("Masukkan nama : ")
print("data = ", data, "type = ", type(data ))

# Mengambil data int dan float
angka = int(input("masukkan angka :"))
print("data = ", angka, "type = ", type(angka))
angka = float(input("masukkan angka :"))
print("data = ", angka, "type = ", type(angka))

# Mengambil data boolean
biner = bool(int(input("masukkan nilai boolean :")))
print("data = ",biner, "type = ",type(biner))