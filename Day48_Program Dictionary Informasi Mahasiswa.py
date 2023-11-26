# Program dictionary informasi Mahasiswa

# Membuat dictionary untuk menyimpan informasi Mahasiswa
siswa = {
    'nama': 'Samsinar',
    'umur': 20,
    'kelas': 'Statistika C',
    'nilai': {
        'Pengantar Bayesian': 95,
        'Komputasi Statistik Laniut': 90,
        'Data Mininh': 91
    }
}

# Menampilkan informasi siswa
print("Informasi Mahasiswa:")
print("Nama:", siswa['nama'])
print("Umur:", siswa['umur'])
print("Kelas:", siswa['kelas'])
print("Nilai:")
for makul, nilai in siswa['nilai'].items():
    print(f"{makul}: {nilai}")