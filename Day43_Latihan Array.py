# Import library NumPy
import numpy as np

# Buat array kosong
array = np.array([])

# Tambahkan isi array secara manual
while True:
    # Minta input data
    data = input("Masukkan data: ")

    # Jika data kosong, hentikan looping
    if data == "":
        break

    # Tambahkan data ke array
    array = np.append(array, data)

# Tampilkan isi array
print("Isi array:", array)

# Hapus data dari array
while True:
    # Minta input indeks data yang akan dihapus
    index = int(input("Masukkan indeks data yang akan dihapus: "))

    # Jika indeks tidak valid, hentikan looping
    if index < 0 or index >= len(array):
        break

    # Hapus data dari array
    array = np.delete(array, index)

# Tampilkan isi array
print("Isi array setelah dihapus:", array)