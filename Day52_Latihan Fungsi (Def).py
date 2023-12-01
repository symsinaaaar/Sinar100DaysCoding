daftar_mahasiswa = []

def tambah_mahasiswa(nama, nim, jurusan):
    mahasiswa_baru = {'Nama': nama, 'NIM': nim, 'Jurusan': jurusan}
    daftar_mahasiswa.append(mahasiswa_baru)
    print(f"Mahasiswa {nama} dengan NIM {nim} dan jurusan {jurusan} berhasil ditambahkan.")

tambah_mahasiswa("Samsinar", "2211302", "Statistika")
tambah_mahasiswa("Flora", "2211312", "Manajemen")
tambah_mahasiswa("Reasyahra","2211317","Keperawatan")

def tampilkan_daftar_mahasiswa():
    if not daftar_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for mahasiswa in daftar_mahasiswa:
            print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}, Jurusan: {mahasiswa['Jurusan']}")

tampilkan_daftar_mahasiswa()