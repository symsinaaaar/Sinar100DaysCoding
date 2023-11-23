# copy dictionary

teman_teman ={
    "Sinar":"Samsinar",
    "Juli":"julianti",
    "Mentari":"Sinar mentari",
    "Flo":"Flora Anastasya",
    "Lala":"Lala Kumala"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["Sinar"]="Sinar Anak Pintar"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataSinar = friends.pop("Sin")
print(f"data sinar = {dataSinar}\n")
print(f"friends = {friends}\n")

# popitem dictionary (mengambil data yang terakhir)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")