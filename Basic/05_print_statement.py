# More ABout print Statements


# We can use both single or double quotes for Printing strings 
# print("Welcome to the python course")
# print('Welcome to the python course')


# We can also print multi-line string in print statement
# print(''' In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available. ''')

# print Multiple values in print statement
# print("Hello", "Pakistan", "Cricket")

# sep property inside print statement
# print("Hello", "Pakistan", "Cricket", sep="$")

# end="" Property of print

# print("This text is printed using python print statement", end=" | ")
# print("And This text is also printed using python print statement")


# Print Shapes USing print Statements 
print("*****************")
print("*               *")
print("*               *")
print("*               *")
print("*               *")
print("*****************")

# print payramid shape using print statements

print("    *   ")
print("   ***   ")
print("  *****   ")
print(" ********   ")


# The end keyword in print statement

""" 
The end keyword in the print statement allows you to specify what character or string should be appended at the end of the printed output instead of the default newline character ('\n').

By default, the end parameter is set to '\n', which means that each call to print ends with a newline character and starts a new line.
"""

# Example: 
print("Hello", end=" ")
print("World", end="!")

# By default every print statements print on new line. but when we use end="" 
# the new line print after where first line finish

print("welcome to Python course.", end=" ")
print("I am from Pakistan", end=" ")
print("I am from Pakistan")



# Seprator
# The sep keyword in the print statement allows you to specify what character or string should be appended
# between each argument in the printed output.

print("Hello World", "Arslan", "programmer", sep=" - ")

# the print statement prints "Hello" and "World" with a hyphen (-) as the separator, resulting in the output "Hello-World".



