# text data - string
# numeric types - integer, float
# squence types: list, tuples, range
# mapping type: dict
# boolen type: true or false

# data type show code
x = 5
print(type(x))

# string
x = "Hello Class"

# İnteger; can be negative
x = 5

# Float
x = 1.4

# List
x = ["banan", "apple", "cheery"]

# Range; shows numbers till the number that written
x = range(5)

# Dictionary; can storage more than one data, can storage diffirent types of data ( integer,string,boolen,float,etc.)
x = {
    "name" : "John",
    "Surname": "Smith",
    "age": 42
}

# Boolen is true or false
x = bool(4)

# İmport; can call module

# " and ' is same
x = "Abdurrahman"
x = 'Abdurrahman'

# Redline is error

# """ you can write multiple lines of notes
"""
dksawdasldkasldas
klasdkşalkdlsşakdalş
laskdlşaksdldksaşldk
"""

# string are arrays
x = "How are you today"
print(x[1]) # prints o

# İmportant note ; index starts with 0

# for repeatly prints every index one by one till it finish
for x in "kemal":
    print(x)

# len ; gives the length of the list or index numbers in the string
a = "Abdurrahman"
print(len(a))

txt = "Abdurrahman has a pc"
print("pc" in txt)

if "pc" in txt:
    print("yes, pc is in it")

# string slicing
x = "Hello Class!"
print(x[:7]) # starts at the beginning bcz there is no number

z = "Hello Class!"
print(z[2:])

# negative index
x = "Hello Class!"
print(x[-5:-2])

# upper case
a = "Abdurrahman"
print(a.upper())

# lower case
a = "ABDURRAHMAN"
print(a.lower())

# strip()
x = " Abdurrahman Karaca "
print(x.strip())

# replace(
a = "Abdurrahman"
print(a.replace("r", "p"))

# split()
x = "Abdurrahman Karaca,Eren Yıldız,Kuzey Yıldız"
print(x.split(","))

# concatenation
a = "Eren "
b = "Kocaömer"
c = a + b
print(c)

c = a + " " + b
print(c)

age = 18
name = "My name is Bengisu, I am" + age
print(name)

# f string
age = 18
name = f"My name is Bengisu, I am {age}"
print(name)

price = 80
x = f"car price is {price} turkish lira"
print(x)

price = 65
txt = f"the price is {price:.2f} dollars"
print(txt)

txt = f"the price is {50 + 90} dollars"
print(txt)

# txt = "I am a lecturer."kemal" " wrong

txt = "I am a lecturer. \"kemal\" " # correct
print(txt)

# boolean values
# true or false
print( 10 > 9)
print( 10 == 9)
print(10 < 9)

a = 250
b = 50

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# evaluate values
#True
bool("hi")
bool(15)
bool("abc")
bool(123)
bool(["appel", "orange"])

#False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])

def myFunction():
    return True

print(myFunction())

def myFunction():
    return True

if myFunction():
    print("yes")
else:
    print("no")

x = 120
print(isinstance(x, str))

# operators
# + addition
# - subtraction
# * multiplication
# / division
# +=   x + = 3   x = x + 3

x = 100
x += 3
print(x)

x = 100
x -= 3
print(x)

x = 100
x *= 3
print(x)

# == equal x == y
# != not equal x !=y
# >= greater than or equal to x >= y
# <= less than or equal to z <= y

x = 3
y = 3
print(x == y)

x = 3
y = 3
print(x != y)

# and operator
print(x < 4 and x < 10)
print(x > 1 and x < 4 and x < 10)

# or operator
x = 2
print(x < 4 or x > 10)

# not operator
x = 4
print(not(x < 5 and x < 10))
x = 5
print(not(x < 5 and x < 10))

# is
x = 3
y = 3
print(x is y)

# is not
x = 3
y = 3
print(x is not y)