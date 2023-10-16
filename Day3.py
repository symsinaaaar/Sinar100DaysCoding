#Tipe data
#angka Satuan(integer)
data_integer = 3
print("data : ", data_integer)
print("-bertipe : ", type(data_integer))

#angka dengan koma(float)
data_float = 1.5
print("data : ", data_float) 
print("-bertipe : ", type(data_float))

#kumpulan karakter(string)
data_string = "Sinar"
print("data : ", data_string)
print("-bertipe : ", type(data_string))

#biner true/false(boolean)
data_bool = True
print("data : ", data_bool)
print("-bertipe : ", type(data_bool))

data_bool = False
print("data : ", data_bool)
print("-bertipe : ", type(data_bool))

#tipe data khusus
#bilangan kompleks
data_complex = complex(1,2)
print("data : ", data_complex)
print("-bertipe : ", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double 
data_c_doubel = c_double(5.5)
print("data: ", data_c_doubel)
print("-bertipe : ", type(data_c_doubel))