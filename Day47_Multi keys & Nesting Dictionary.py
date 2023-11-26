import datetime

mahasiswa1 = {
    'nama':'sinar',
    'nim':'E0221302',
    'sks':88,
    'beasiswa':'True',
    'lahir':datetime.datetime(2003,8,13)
}

mahasiswa2 = {
    'nama':'julianti',
    'nim':'E0221302',
    'sks':88,
    'beasiswa':'True',
    'lahir':datetime.datetime(2003,7,27)
}

mahasiswa3 = {
    'nama':'mentari',
    'nim':'E0221302',
    'sks':88,
    'beasiswa':'false',
    'lahir':datetime.datetime(2003,7,13)
}

data_mahasiswa = {
    'key1':mahasiswa1,
    'key2':mahasiswa2,
    'key3':mahasiswa3
}
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<5} {'Beasiswa':<5} {'Lahir':<15}")
print("_"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<5} {'BEASISWA':<5} {'LAHIR':<15}")
    print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<5} {'BEASISWA':^5} {'LAHIR':<15}")