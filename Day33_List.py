## --- LIST --- ##

# Kumpulan data numbers
data_angka = [1, 5, 2, 3]
print(data_angka)

# Kumpulan data string
data_string = ["Sinar", "Juli", "Mentari"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "bala-bala", 2, "cireng", "Sinar", True, "Juli", False]
print(data_campuran)

## cara alternatif membuat List
data_range = range(0,10) # range(start, stop)
data_list = list(data_range)
print(data_list)

data_range = range(0,10,2) # range(start, stop, step)
data_list = list(data_range)
print(data_list)

## membuat list dengan for loop, list comprehension
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

## membuat list pake for pake if 
list_pake_for_if = [i for i in range(0,10) if i!= 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2!= 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2!= 0]
print(list_pake_for_if)