## pengenalan String
# cara membuat string
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = " Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \
# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Sinar")

# tab
print("sinar\t\t\tMentari, semakin jauhan")

# backspace
print("Sinar \bmatahari, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> Line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> Carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF Line feed carriage return -> dipakai oleh windows


# 3. String Literal atau Raw
# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunkan raw string
print(r'C:\new folder')

# multiline Literal string
print("""
Nama : Sinar
Jurusan : Statistika
""")

# multiline Literal string
print(r"""
Nama : Sinar
Jurusan : Statistika
Website : www.sinar.com/NewID
""")