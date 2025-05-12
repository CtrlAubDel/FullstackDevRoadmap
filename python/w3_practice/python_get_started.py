import sys
import random

print("Hello, world!")
print("Python version: " + sys.version)
if 5 > 2: 
    print("Five is greater than two") # This is an inline comment!
x = str(5)
y = "Aubrey"
print("X equals " + x)
print("Y equals " + y)
print(type(x))
print(type(y))

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
#2myvar = "John"
#my-var = "John"
#my var = "John"

#Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Pear"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Aubrey"
y = 24
print(x, "is", y, "years old")

randomWord = "awesome"

def myfunc():
    print("Python is " + randomWord)

myfunc()

def myfunc():
    global randomWord
    randomWord = "cool"
    print("Python is " + randomWord)

myfunc()

print(randomWord)
#The following will print a random number between the provided range
print(random.randrange(1,100))

x = "Hello, World!"
print(x[12])

for x in "banana":
    print(x)