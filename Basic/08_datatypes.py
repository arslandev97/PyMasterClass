# Built in data types

# Variables can store data of different types, and different types can do different things

# Python has following data types

'''
Text type       :   str
Numeric Types   :   int, float, complex
Sequence Types  :   list, tuple, range
Mapping Type    :   dict
Set Types       :   set, frozenset
Boolean Types   :   bool
Binary Types    :   bytes, bytearray, memoryview
None Type       ;   none

'''

# Get the type of variable 
# type()

# str 
name = "Arslan"
print(name, type(name))

# Numeric Types ---> int, float, complex

# int 
x = 20      # int 
y = 21.5    #float 
z = 1j      #complex
z = 1 + 8j  #complex

print(x, type(x))
print(y, type(y))
print(z, type(z))


# Sequence Types ---> list, tuple, range

# list
items = ["Mobile", "Laptop", "Macbook", "Pc"]
print(items)
print(type(items))

# Tuple 
items = ("Mobile", "Laptop", "Macbook", "Pc")
print(items)
print(type(items))


# Mapping Type ---> dict
student = {
    "name": "Ali Raza",
    "age" : 20,
    "subject" : "CS"
}
print(student)
print(type(student))

# Set Types ---> Set Frozen Set

items = {"Mobile", "Laptop", "Macbook", "Pc"}
print(items)
print(type(items))

# Frozen Set

items = ({"Mobile", "Laptop", "Macbook", "Pc"})
print(items)
print(type(items))

# Boolean 

x = 5 > 8
booool = True
print(x)
print(type(x))

# None Type 

name = None
print(name, type(name))

