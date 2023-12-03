'''Default Argument'''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya)


def say_hello(nama = "Manis"):
    '''fungsi dengan default argument'''
    print(f"Hallo {nama}")


say_hello("Sinar")
say_hello()

def sapa_dia(nama,pesan):
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"Hai {nama}, {pesan}")

sapa_dia("Sinar", "Hai manis")

def sapa_dia(nama, pesan = "Apa kabar?"):
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"Hai {nama}, {pesan}")

sapa_dia("Hai Manis", "Sinar")
sapa_dia("Juli")

# contoh 3

def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=2, angka=5)
print(hasil)

# contoh 4

def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil
print(fungsi())
print(fungsi(input3=10))