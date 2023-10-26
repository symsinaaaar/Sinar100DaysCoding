# String width and Alignment
# Width and Multiline
# Data
data_nama = "Sinar Mentari"
data_umur = 21
data_tinggi = 164.5
data_nomor_sepatu = 49

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data_string"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data_string"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
"""
print("\n"+5*"="+"Data_string"+5*"=")
print(data_string)

data_string = f"""
nama = {data_nama} , umur = {data_umur}
"""
print("\n"+5*"="+"Data_string"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Sinar"
data_string = f"""
nama    = {data_nama}
nama    = {data_nama:>10}
umur    = {data_umur:>10}
tinggi  = {data_tinggi:>10}
sepatu  = {data_nomor_sepatu:>10}
"""
print("\n"+5*"="+"Data_string"+5*"=")
print(data_string)