"""
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType

"""
# Obtendo o tipo de dados:
# Você pode obter o tipo de dados de qualquer objeto usando a função type():

# Exemplo:
x = 5
print(type(x))


x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x))

# Saída esperada: 

# Hello World
# <class 'str'>

x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# Saída esperada: 
# 20
# <class 'int'>



x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# Saída esperada: 
# 20.5
# <class 'float'>



x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# Saída esperada: 
# lj
# <class 'complex'>


x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x))
# Saída esperada:
# ['apple', 'banana', 'cherry']
# <class 'list'> 


x = ("apple", "banana", "cherry")

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# Saída esperada:
# ('apple', 'banana', 'cherry')
# <class 'tuple'>

x = range(6)

#display x:
print(x)

#display the data type of x:
print(type(x))

# Saída esperada:
# range(0, 6)
# <class 'range'>

x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# Saída esperada:
# {'name': 'John', 'age': 36}
# <class 'dict'>

x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x))

# Saída esperada:
# {'apple', 'banana', 'cherry'}
# <class 'set'> 

x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# Saída esperada:
# frozenset({'banana', 'apple', 'cherry'})
# <class 'frozenset'>

x = True

#display x:
print(x)

#display the data type of x:
print(type(x))

# Saída esperada:
# True
# <class 'bool'> 


x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x))

# Saída esperada:
# b'Hello'
# <class 'bytes'> 


x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# Saída esperada:
# bytearray(b'\x00\x00\x00\x00\x00')
# <class 'bytearray'>



x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x))

# Saída esperada:
# <memory at 0x00A78FA0>
# <class 'memoryview'>

x = None

#display x:
print(x)

#display the data type of x:
print(type(x))

# Saída esperada:

#None
# <class 'NoneType'>


