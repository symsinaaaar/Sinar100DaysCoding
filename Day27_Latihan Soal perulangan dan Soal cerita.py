# Soal perulangan dan Soal cerita
nama = "Sinar"
for i in range(1,11):
    print(f"{i}.{nama}")
print("akhir dari program \n")

#juhari ingin membeli sebuah lahan dengan ukuran 10x15 sejumlah 30 kampling yang berbeda tempat
#setiap meter persegi dari tanah tersebut berharga 500.000 hitunglah total keseluruhan Harga

# luas lahan per kampling
luas_per_kampling = 10 * 15

# harga per meter persegi
harga_per_meter_persegi = 500000

# Hitung total harga per kampling
total_harga_per_kampling = luas_per_kampling * harga_per_meter_persegi

# total harga keseluruhan
total_harga_keseluruhan = total_harga_per_kampling * 30

# total harga keseluruhan
print("Total harga keseluruhan:", total_harga_keseluruhan)