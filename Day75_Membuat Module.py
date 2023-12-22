# module matematika dengan import

from matematika import tambah,kali,pangkat

hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"hasil pangkat 3 = {pangkat_3(3)}")

# contoh menggunakan alias
from matematika import tambah as plus
from matematika import kali as times
from matematika import pangkat as kuadrat

hasil_tambah = plus(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = times(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = kuadrat(3)
print(f"hasil pangkat 3 = {pangkat_3(3)}")