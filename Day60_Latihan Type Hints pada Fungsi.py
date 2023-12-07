def hitung_bmi(berat_badan: float, tinggi: float) -> float:
    bmi = berat_badan / (tinggi ** 2)
    return bmi

# Input dari pengguna
berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi (m): "))

bmi = hitung_bmi(berat_badan, tinggi)

print(f"BMI Anda adalah: {bmi:.2f}")

# Menyediakan kategori BMI umum
if bmi < 18.5:
    kategori = "Kurus"
elif 18.5 <= bmi < 24.9:
    kategori = "Normal"
elif 25 <= bmi < 29.9:
    kategori = "Gemuk"
else:
    kategori = "Obesitas"

print(f"Kategori BMI Anda: {kategori}")