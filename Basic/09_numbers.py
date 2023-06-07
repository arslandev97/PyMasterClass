# Python Numbers

# There are three types of numbers in python
# 1. int
# 2. float
# 3. complex

x = 20      # int 
y = 21.5    #float 
z = 1j      #complex
z = 1 + 8j  #complex

print(x, type(x))
print(y, type(y))
print(z, type(z))


# 1. int
# int, or integer, is a whole numbers, positive or negative, whichout decimal numbers, of unlimited length

x = 1
y = 325545645184454154
z = -323232521

print(x, type(x))
print(y, type(y))
print(z, type(z))


# 2. float 
# float, or floating point numbers, is a numbers of positive or negative, which decimal numbers

x = 1.10
y = 1.0
z = -31.79

print(x, type(x))
print(y, type(y))
print(z, type(z))

a = 32E2
b = -67.55e100
print(a, type(a))
print(b, type(b))


# 3. complex

ax = 1j      #complex
bx = 1 + 8j  #complex

print(ax, type(ax))
print(bx, type(bx))


# Type Conversion

x = 1
y = 12.5
z = 1j

# convert from int to float:
a = float(x)
print(a, type(a))


# convert from float to int:
b = int(y)
print(b, type(b))


# convert from int to complex:
c = complex(x)
print(c, type(c))


# convert from complex to int:
# cannot convert complex to int : it will generate an error
d = int(c)
print(d, type(d))

z = int("10")
z = int(2.3)



# Random Number Moudule

import random

# random_number = random.randrange(0, 2)
# print(random_number)

# Toss ---> coin flip  --> games (cricket, Football, hockey, etc)

toss = random.randrange(0, 2)

if(toss == 0):
    print("tail")
else:
    print("head")

# head = 1
# tail = 0


# Dice Roll ---> Ludo game

# 1 dice roll has 6 sides 

# side1 = 1
# side2 = 2
# side3 = 3
# side4 = 4
# side5 = 5
# side6 = 6

