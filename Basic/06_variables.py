# Python Variables

# VAriables are the container for storing some data

# HOw to create a variable

# Syntax
# variable_name = value 
# Python Variables are dynamic type

# different types of data to be store in varibales

# "Welcome"     --> String 
# 123           --> int 
# 12.5          --> float
# true, false   --> Boolean


# create a variable
# Python has no command for declaring a variable

# String Variables
person_name = "Arslan"
print(person_name)


# Integer Variables
x = 10
y = 20
z = x + y
print(x, end="\t")
print(y, end="\t")
print(z)

# pii = int(3.14)
# print(pii)


# Float 
pi = 3.14
print(pi)


# How to check variables data type

employee_Name = "Ali"
print(employee_Name)
print(type(employee_Name)) # we use type() function to check veriables type

marks = 87
print(marks)
print(type(marks))
print(marks, type(marks)) # we can print both on the same line

print("Student Marks :", marks, type(marks))
print("Student Marks :", marks, " and Variable type is ", type(marks))


# Variable Type Casting

""" 
Type casting, also known as type conversion, is the process of changing the data type of a variable from one type to another 
It allows you to convert a value from its current data type to a different data type, enabling you to perform specific operations or assignments that require a different type.

"""


a = "10"
b = "20"
print(a+b) # output : 1020
print( int(a) + int(b)) # output : 30

# checking the type of original variables
print(type(a), type(b))

# Type cast variable from string to int
a = int(a)
b = int(b)

# Checking again after typecasting the original values
print(type(a), type(b))
print(a+b) # output : 30


# Example : Type casting

x = str(3)
y = int(7.14)
z = float(5)

print(x, y, z)

