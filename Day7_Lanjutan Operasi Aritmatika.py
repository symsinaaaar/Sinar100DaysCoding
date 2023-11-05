##Lanjutan Operasi Aritmatika

# Prioritas Operasi, Operational Precedence
'''
    1. ()
    2. **
    3. *, /, %, //
    4. +, -
'''
x = 7
y = 5
z = 3

hasil = x + y * z
print(x,'+',y,'*',z, '=', hasil)

hasil = (x + y) * z
print(x,'+',y,'*',z, '=', hasil)

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)
