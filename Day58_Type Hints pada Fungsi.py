'''Type Hints Untuk Fungsi'''

# bentuk standar fungsi yang sudah di pelajari

def fungsi(parameter):
    print(parameter)

fungsi(1)
fungsi("Ucup")
fungsi(True)


# penggunaan type hints
import string

def fungsi_dengan_hints(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = fungsi_dengan_hints(4)
print(HASIL)

def display(argument:string):
    print(argument)

display("Sinar")
