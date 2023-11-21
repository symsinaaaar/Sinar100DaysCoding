# operasi dictionary

data_dict = {
    "Sinar":"Samsinar",
    "Juli":"julianti",
    "Mentari":"Sinar mentari"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "Sinar"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["Sinar"])
print(data_dict.get("Sinar"))
print(data_dict.get("Flo","key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["Sinar"] = "Sinar si pintar"
print(data_dict)
data_dict["Flo"] = "Flo kupu-kupu"
print(data_dict)

data_dict.update({"Sinar":"Samsinar"})
print(data_dict)
data_dict.update({"Lala":"Lala Kumala"}) # jika tidak ada di add aja
print(data_dict)

# mendelete data pada dictionary
del data_dict["Flo"]
print(data_dict)