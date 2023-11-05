#daftar buah yang di beli dalam satuan kg 
apel = 20
anggur = 18
rambutan = 17
jeruk = 29

# harga apel
harga_1apel = 5000
berat_1apel_gram = 200
total_berat_apel = apel * 1000
jumlah_apel = total_berat_apel / berat_1apel_gram
harga_apel = jumlah_apel * harga_1apel
print("Harga apel Rp.",harga_apel)

# harga anggur
harga_100g_anggur = 3000
total_berat_anggur = anggur * 1000
jumlah_anggur = total_berat_anggur / 100
harga_anggur = jumlah_anggur * harga_100g_anggur
print("Harga anggur Rp.",harga_anggur)

# harga rambutan
harga_1kg_rambutan = 15000
harga_rambutan = rambutan * harga_1kg_rambutan
print("Harga rambutan Rp.",harga_rambutan)

#harga jeruk
harga_3kg_jeruk = 45000
jumlah_jeruk = jeruk / 3
harga_jeruk = jumlah_jeruk * harga_3kg_jeruk
print("Harga jeruk Rp.",harga_jeruk)

# harga semua buah
harga_total = harga_apel + harga_anggur + harga_rambutan + harga_jeruk
print("Harga semua buah Rp.",harga_total)

# total bonus
bonus = (apel // 5) + (anggur // 5) + (rambutan // 5) + (jeruk // 5)
total_bonus = bonus * 0.5
print("Bunus yang di dapatkan dari masing-masing buah sebesar ",total_bonus," Kg")

# diskon 0.2% untuk buah > 20Kg
diskon_jeruk = harga_jeruk * 0.002
print("Diskon untuk buah jeruk karena melebihi 20Kg senilai Rp.",diskon_jeruk)

# total bayar
total_bayar = (harga_total - diskon_jeruk) + total_bonus
print("Total pembayaran Ucup pada toko SEJAHTERA sebesar Rp.",total_bayar)