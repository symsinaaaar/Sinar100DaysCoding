def konversi_celsius_ke_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def konversi_fahrenheit_ke_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Input dari pengguna
suhu_celsius = float(input("Masukkan suhu dalam Celsius: "))
suhu_fahrenheit = konversi_celsius_ke_fahrenheit(suhu_celsius)

print(f"{suhu_celsius} Celsius setara dengan {suhu_fahrenheit:.2f} Fahrenheit")

suhu_fahrenheit_input = float(input("Masukkan suhu dalam Fahrenheit: "))
suhu_celsius_output = konversi_fahrenheit_ke_celsius(suhu_fahrenheit_input)

print(f"{suhu_fahrenheit_input} Fahrenheit setara dengan {suhu_celsius_output:.2f} Celsius")