# Deklarasi variabel
nama = "Sinar"
password = "260421"

# Menu
print("""
1. Login
2. Edit Username/Password
3. Register
4. Exit

Pilih menu: """)
menu = input()

# Proses login
if menu == "1":
  print("""
Username: """)
  username = input()
  print("""
Password: """)
  password_input = input()

  if username == nama and password_input == password:
    print("""
{} kamu telah berhasil login!
""".format(nama))
  else:
    print("""
Username dan Password anda salah!
""")

# Proses edit username/password
if menu == "2":
  print("""
Username baru: """)
  username_baru = input()
  print("""
Password baru: """)
  password_baru = input()

  # Ubah username dan password di variabel
  nama = username_baru
  password = password_baru

  print("""
Username dan Password berhasil diubah!
""")

# Proses register
if menu == "3":
  print("""
Username: """)
  username = input()
  print("""
Password: """)
  password = input()

  # Simpan username dan password ke variabel
  nama = username
  password = password

  print("""
Registrasi berhasil!
""")

# Proses keluar
if menu == "4":
  print("""
Terima kasih telah menggunakan aplikasi ini!
""")

# Jika menu tidak valid
if menu not in ["1", "2", "3", "4"]:
  print("""
Menu yang anda pilih tidak valid!
""")