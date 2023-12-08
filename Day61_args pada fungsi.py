'''*args'''

# *args
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Sinar", 164,60)

# studi kasus
def tambah(*data):
    # data tipenya adalah tuple, bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    return output
hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"hasil = {hasil}")