#casting data 
##INTEGER
print("====INTEGER====")
data_int   = 3
print("data : ", data_int, "type =", type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
print("data : ", data_float, "type =", type(data_float))
print("data : ", data_str, "type =", type(data_str))
print("data : ", data_bool, "type =", type(data_bool))

##FLOAT
print("====FLOAT====")
data_float = 3.5
print("data : ", data_float, "type =", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data : ", data_int, "type =", type(data_int))
print("data : ", data_str, "type =", type(data_str))
print("data : ", data_bool, "type =", type(data_bool))

##BOOLEAN
print("====BOOLEAN====")
data_bool = True
print("data : ", data_bool, "type =", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data : ", data_int, "type =", type(data_int))
print("data : ", data_str, "type =", type(data_str))
print("data : ", data_float, "type =", type(data_float))

print("====BOOLEAN====")
data_bool = False
print("data : ", data_bool, "type =", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data : ", data_int, "type =", type(data_int))
print("data : ", data_str, "type =", type(data_str))
print("data : ", data_float, "type =", type(data_float))

##STRING
print("====STRING====")
data_str = "Sinar dan Juli"
print("data : ", data_str, "type =", type(data_str))

#data_int = int(data_str) -> str harus angka
#data_float = str(data_str) -> str harus angka
data_bool = bool(data_str)
print("data : ", data_int, "type =", type(data_int))
print("data : ", data_float, "type =", type(data_float))
print("data : ", data_bool, "type =", type(data_bool))
