#sebuah perpustakaan memiliki 3 area Pengambilan Buku 
#ada area A, area B, dan area C
#Kondisi :dimana area A berisi Novel, 
#area B berisi Komik dan area C berisi majalah
#buatkan inputanJenisBukudan Area Pengambilan jika 
#pengguna menginputkan JenisBuku dan Area Pengambilan 
#yang sesuai dengan kondisi di atas maka akan menghasilkan
#output "Benar"jika tidak sesuai dengan kondisi di atas maka menghasilkan output "Salah"


areaPengambilan= input("Masukkan area pengambilan : ")
jenisBuku = input("Masukkan jenis buku : ")

if areaPengambilan == "Area A" and jenisBuku == "Novel":
    print("Benar")
elif areaPengambilan == "Area B" and jenisBuku == "Komik":
    print("Benar")
elif areaPengambilan == "Area C" and jenisBuku == "Majalah":
    print("Benar")
else:
    print("Salah")