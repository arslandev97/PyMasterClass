# More About Python Variables

# Rules for declaring variables
# 1. Variable name must start with alphabet or underscore character

# Correct Syntax

student_name = "Ali"
_student_name = "Ali"
_7student_name = "ALi"

# 2. Variable name cannot start with number
# incorrect syntax

# *student = ""
# 7student = ""


# 3. You can use alphanumeric values as variable name like (0-9, a-z, A-Z, _)
student_1 = "Wajdan"
student_2 = "Ahmed"
_3_Student = "Ibraheem"


# 4. Python variables are Case Sensitive
a = 10
A = 20

# print("a = ",a)
# print("A = ",A)

# print("a = "+ str(a))
# print("A = "+ str(A))


# 5. Cannot use Python Reserved keywords as a variable name 
# and 
# as 
# assert 
# print 
# int
# continue 
# break
# & many more


# 6. White spaces should not bhe included in variable names
# full name = "Arslan Yousaf" # incorrect syntax


# 7. variable names should be descriptive  [optional]
my_full_name = "Muhammad Arslan"

# --------------------------------------------------- #

# Python variable names writing Sytles / Conventions  

# 1. Snake Case 

full_name = "Ali"
student_name = "Hamza"
employee_name = "Basit"


# 2. Camel Case 

fullName = "Arslan"
studentName = "Hamza"
employeeName = "Fahad"


# 3. Pascal Case

FullName = "Arslan"
FtudentName = "Hamza"
EmployeeName = "Fahad"


# Many Values to Many Variables
x = 10
y = 20
z = 30

# Write them in a single line
x, y, z = 10, 20, 30
print (x, y, z)

student_name, student_marks, student_grade = "Arslan", 87, "A"
print(student_name)
print(student_marks)
print(student_grade)


# one value assign to multiple variables  
x = y = z = 0
print(x, y, z)


# unpack 
number = [1,2,3]
x, y, z = number
print(x, y, z)


# Update variable values
x = 20
y = 30

print(x, y)

x = 100
y = 150.5

print(x, y, type(y))


