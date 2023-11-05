# Operasi dan manipulasi string #
# mengubah case dari string
# mengubah semua ke upper case

salam = "sist!"
print("normal =" + salam)
salam = salam.upper()
print("upper = " + salam)

# mengubah semua ke lower case
alay = "aKu KeRen BangetTTTT"
print("normal = " + alay)
alay = alay.lower()
print("lower = " +alay)

## pengecekan dengan isX method
# contoh pengecekan lower case
salam = "bro"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <--- untuk mengecek semuanya huruf
# isalnum() <--- huruf dan angka
# isdecimal() <--- angka saja
# isspace() <--- spasi, tab, newline \n
# istitle() <--- semua kata dimulai dengan huruf besar

judul = "It Is Okay To Not Be Okay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endawith() <--- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','syang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ''.join(pisah)
print(gabungan)

gabungan = 'ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter
print(5*"=" + "data" + "="*5)
# alokasi karakter rjust(), ljust() center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

matahari = "matahari".rjust(10)
print("'"+matahari+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

matahari = "matahari".ljust(10)
print("'"+matahari+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(10,"-")
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip()
print("'"+tengah+"'")

kanan = "kanan".strip()
print("'"+kanan+"'")

kiri = "kiri".strip()
print("'"+kiri+"'")






