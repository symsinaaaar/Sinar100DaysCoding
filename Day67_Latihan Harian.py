# Global dan local scope

# Variabel global
total_pendapatan = 1000000

# Fungsi menghitung bonus berdasarkan pendapatan global
def hitung_bonus():
    bonus = total_pendapatan * 0.1  # Variabel lokal scope
    return bonus

# Fungsi menampilkan total pendapatan dan bonus
def tampilkan_informasi():
    print(f"Total Pendapatan: {total_pendapatan}")
    print(f"Bonus: {hitung_bonus()}")

tampilkan_informasi()

# Mengubah total pendapatan dan menampilkan informasi lagi
total_pendapatan = 1500000
tampilkan_informasi()

# Fungsi dengan variabel lokal yang memiliki nama yang sama dengan variabel global
def fungsi_dengan_variabel_lokal_sama():
    total_pendapatan = 2000000
    print(f"Total Pendapatan di dalam fungsi: {total_pendapatan}")

fungsi_dengan_variabel_lokal_sama()

# Menampilkan total pendapatan setelah pemanggilan fungsi di atas
print(f"Total Pendapatan setelah fungsi: {total_pendapatan}")