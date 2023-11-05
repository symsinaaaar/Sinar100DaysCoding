# Operasi dan Manipulasi string #

# 1. Menyambung String (Concatenate)
nama_pertama = "Sinar"
nama_tengah = "Mentari"
nama_akhir = "Bersinar"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)
nama_lengkap = nama_pertama + " "  + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung Panjang String
panjang = len(nama_lengkap)
print(panjang)
print("panjang dari" + nama_lengkap + " = " + str(panjang))

# 3. Operator Untuk String
# Mengecek apakah ada komponen char atau string di string
S = "Sinar"
status = S in nama_lengkap
print("string" + S + "ada di" + nama_lengkap + " = " + str(status))

S = "sinar"
status = S in nama_lengkap
print("string" + S + "ada di" + nama_lengkap + " = " + str(status))

S = "sinar"
status = S not in nama_lengkap
print("string" + S + "tidak ada di" + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:5]:" + nama_lengkap[0:5])
print("index ke-[0:5]:" + nama_lengkap[0:6])
print("index ke[0,2,4,6,8,10]:" + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 15
print("char untuk ASCII 15 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "Sinar Matahari"
jumlah = data.count("i")
print("jumlah i pada " + data + " = " + str(jumlah))