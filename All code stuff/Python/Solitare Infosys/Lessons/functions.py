# A function is a block of code defined by the keyword, followed by the function name, further being followed by parameter and ":".

# A function can't be executed untill or unless it is called.
 
# A function can be called from anywhere in the program once defined.

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

def functioname(a,b):
    print(a,",",b)
    
def add1(a,b):
    print(a+b)
    
functioname(5,6)
print()

add1(5,6)
print()

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

# arbitrary arguments: when you dont know the number of arguments that will be passed at the time of function call, then just add * before the parameter

def add2(*brands):
    print(brands)
    
add2('nike','adidas','gucci')
print()

# ------------------------------------------------------------------- #

# keyword arguments: Automatically arranges the list according to the keywords specified.

def add3(child1,child2,child3):
    print(child1,',',child2,',',child3)

add3(child2='Harry',child3="Raj",child1="Shiv")
print()

# ------------------------------------------------------------------- #

# arbitrary keyword arguments: when you dont know the number of arguments that will be passed at the time of function call, then just add ** before the parameter

def add4(**child):
    print(child)
    
add4(child1="Shiv",child2='Harry',child3="Raj")
print()

# ------------------------------------------------------------------- #

# default argument: Prints already mentioned values if no inputs given, else uses the user added values.

def country(name="India"):
    print(name)
    
country("USA")
country()
country("Japan")
print()

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

# file handling

# x: create
# w: write
# r: read
# a: append

# ------------------------------------------------------------------- #

# Creating a file

# file = open('lloll.txt','x')
# file.write('This is a new file')
# file.close()
# print()

# Reading a file.

file = open('lloll.txt','r')
print(file.read())
# print(file.readline(6))
# print(file.readlines(6))
file.close()
print()

# ------------------------------------------------------------------- #

# Writing in a file

file = open("lloll.txt","w")
file.write('This is a writen content')
file.close()
print()

file = open('lloll.txt','r')
print(file.read())
file.close()
print()

# ------------------------------------------------------------------- #

# Appending (Adding) in a file

file = open("lloll.txt","a")
file.write('\nThis is also a writen content')
file.close()
print()

file = open('lloll.txt','r')
print(file.read())
file.close()
print()

# ------------------------------------------------------------------- #

# Checking if the file exists:

import os

if os.path.exists("lol.txt"):
    print("File is present")
    file = open ("lol.txt","r")
    print(file.read())
    file.close()
    print()
    
    os.remove("lol.txt")
    print("File is deleted, Enjoy")
    
else:
    print("File is not present, Creating one....")
    file = open('lol.txt','w')
    file.write('This is an auto-generated message due to the file not being present and created by the program. Enjoy!!!')
    print()
    
    file = open ("lol.txt","r")
    print(file.read())
    file.close()
    print()
# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #
