daftar_mahasiswa = []

def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    jurusan = input("Masukkan jurusan mahasiswa: ")
    
    mahasiswa_baru = {'Nama': nama, 'NIM': nim, 'Jurusan': jurusan}
    daftar_mahasiswa.append(mahasiswa_baru)
    
    print(f"Mahasiswa {nama} dengan NIM {nim} dan jurusan {jurusan} berhasil ditambahkan.")

tambah_mahasiswa()
tambah_mahasiswa()
tambah_mahasiswa()

def tampilkan_daftar_mahasiswa():
    if not daftar_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for mahasiswa in daftar_mahasiswa:
            print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}, Jurusan: {mahasiswa['Jurusan']}")

tampilkan_daftar_mahasiswa()