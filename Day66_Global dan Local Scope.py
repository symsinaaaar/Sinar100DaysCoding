## Global dan local scope

nama = "Sinar" # <- variabel global

# akses variabel global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan {nama}")

fungsi1()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama}")

# percabangan
if True:
    print(f"if menampilkan {nama}")


## variabel local Scope

def fungsi2():
    nama_local = "Mentari" # <- variabel lokal scope

fungsi2()


## contoh penggunaan
def say_Juli():
    print(f"Hello {nama}")

nama = "Juli"
say_Juli()