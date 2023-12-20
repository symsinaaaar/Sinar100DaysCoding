from datetime import datetime

def hitung_umur(tahun_lahir):
    tahun_sekarang = datetime.now().year
    umur = tahun_sekarang - tahun_lahir
    return umur

# Masukkan tahun lahir kamu
tahun_lahir = int(input("Masukkan tahun lahir kamu: "))
umur = hitung_umur(tahun_lahir)

print(f"Umur kamu sekarang adalah {umur} tahun.")