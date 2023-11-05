## Format String ##

# contoh generic
# string
nama = "Sinar"
str = "hello" + nama
print(str)

format_str = f"Hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = "angka = {angka}" 
print(format_str)

format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 10
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.535781
format_str = f"deismal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.535781
format_str = f"deismal = {angka:8.2f}"
print(format_str)

# menampilkan tanda + atay -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)

# memperformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"

print(format_persen)

# melaakukan operasi aritmatika dalam placeholder

harga = 10000
jumlah = 5

format_string = f"harga total = Rp.{harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadesimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
