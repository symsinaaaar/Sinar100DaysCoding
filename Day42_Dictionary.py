# list -> array, mengakses dengan menggunakan index
data_list = ["Sinar", "Juli", "Mentari"]
print(data_list[0])

# dictionary (dict) -> associative array
# identifier -> key
data_dict = {
    'key1':'value1',
    'key2':'value2'
}
print(data_dict)

data_dict = {
    'sr':'sinar',
    'ji':'juli',
    'mi':'mentari'
}
print(data_dict['sr'])

data_dict = {
    'sr':'sinar',
    'ji':'juli',
    'mi':'mentari',
    'number':100,
    'list':data_list
}
print(data_dict['sr'])
print(data_dict['number'])
print(data_dict['list'])