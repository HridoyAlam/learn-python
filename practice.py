'''
nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 3)

words = ["spam", "egg", "chikem", "meat"]
print("spam" in words)
print("tea" in words)

nums = [10,9, 8, 7, 6, 5]
nums[0] = nums[1]-5

if 4 in nums:
    print(nums[3])
else:
    print(nums[4])
print(nums)


nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#list functions
nums = [1, 1, 2, 3]
nums.append(4)
#print(nums)
#print(len(nums))
index = 1
nums.insert(index,9)
print(nums)
#print(nums. index(9))
print( max (nums))
print( min (nums))
print(nums.count(1)) #list.count(item)
nums.remove(9)
print(nums)
nums.reverse()
print(nums)


#while loops
i = 1
while i<= 5:
    print(i)
    i = i+1
print("finished")

i = 3
j = 0
while i >= 0:
    print(i)
    i -=1
    j +=1
print(j)


i = 1
while i<=10:
    if i % 2 ==0:
        print(str(i) + " is a even number")
    else:
        print(str(i) + " is a odd number")

    i +=1

i = 0
while True: # while true is an easy and short way to create infinite loop
    
    
    i = i+1

    if i ==2:
        print("skipping 2")
        continue
        

    if i>=5:
        print("Breaking the loop")
        break
    print(i)

print("finished")


###for loops
words = ["hello", "world", "spam","eggs"]
for i in words:
    print(i + " ! ")

## for loops can be used to iterate over strings

str = "testing for loops"
count = 0

for x in str:
    if (x =="t"):
        count +=1
print(count)

## Range
numbers = list(range(10))
print(numbers)

numbers = list(range(3,8))
print(numbers)
print( range(20) == range(0, 20))


numbers = list(range(5, 20, 2))
print(numbers)

numbers = list(range(20, 5, -2))
print(numbers)

#printing even numbers 0,2,,,,,,18
for i in range(0, 20, 2):
    print(i)


###function
def my_func():
    print("Python")
    print("python")
    print("python")
my_func()

def even(num):
    if (num % 2 == 0):
        print("This is even Number")
    else:
        print("This is odd number")
even(5)

def max_num(x, y):
    if (x > y):
        return x
    else:
        return y
print(max_num(4,5))


##function a object

def multify(x, y):
    return x * y
a = 4
b = 5

operation = multify # creating obejct of multify
print(operation(a, b))


#funtion can also be used as arguments of other functions

def add(x, y):
    return x + y

def do_twice( func, x, y): # do_twice takes a function as its argument and call it in its body
    return func( func(x,y), func(x,y) )


a = 5
b = 10

print(do_twice(add, a, b))

# modules
import random

for i in range(5): #0 to 4
    value = random.randint(1, 6)
    print(value)

from math import pi #import pi from math module
from math import pi, sqrt #import pi & sqrt from math module
from math import* ##import all object from math module
from math import sqrt as square_root
print(square_root(100))
'''
'''
some modules
string, re, datetime, math, random, os, multiprocessing, sub process, socket, 
email, json, doctest, unitest, pdb, argparse, sys


# Exception handling
try:
    a = 7
    b = 0
    print(a/b)
    print("Done calculation")
except ZeroDivisionError:
    print("an error occured")
    print("Due to zero divison")

### A try statement can have multiple different except blocks to handle different exceptions
try:
    var = 10
    print(var + "hello")
    print(var / 2)

except ZeroDivisionError:
    print("divided by zero")
except (ValueError, TypeError):
    print("Error occured")

##code within finally statements always run

try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Division by zero!")
finally:
    print("This code will run no matter what")


#Raising Exeptions 
#you need to specify the type of exception raised
print(1)
raise ValueError
print(2)

try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError


print("123")
raise NameError("Invalid name!")

num = input(":")
if float(num)


###ASserations
print(1)
assert 2+2 ==4
print(2)
assert 1+1 ==3
print(3)

#ASserations can take a second argument that is passed to the assertionError raised if the asserations fails
temp =-10
assert (temp >= 0), "colder than absoulte zero"

# Read file
#opening file
open("file.txt", "w")
#read mode
open("file.txt", "r")
# binary write mode
open("file.txt", "wb")
#both read & write
open("file.txt", "r+")

file = open("file.txt","w")
#do stup to the file
file.close()


#writng file
f = open("file.txt","w")
f.write("this has been writen to the file")
f.close()

f = open("file.txt","r")
print(f.read())
f.close()

msg = "Hello world"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

# good practice to file works in exception
try:
    f = open("filename.txt")
    print(f.read())
finally:
    f.close()


# with statement automatically close 
with open("filename.txt") as f:
    print(f.read())

#Dictionaries
ages = {"dave": 20, "nikhil": 21, "monami": 24 }
print(ages["dave"])


#Trying to index a key that isn;t part of the dictionary returns a KeyError

primary = {
    "red": [25, 0, 0],
    "green": [0, 255, 0]
}
print(primary["red"])
#print(primary["yello"])
print("red" in primary)



#Only immutable objects can be used as keys to ditionaries.
# immutable objects are those can't be changed.

#to get the index of ditionaries <get> is used, if it didn't find it, it's return None 

paris = {
    1 : "apple",
    "orange": [1,2,3],
    True: False,
    None: "True",
}
print(paris.get("red"))
print(paris.get("orange"))
print(paris.get(7))
print(paris.get(12345, "not in dictionary"))

'''
##tuples (immutable)
words = ("span", "eggs", "sausages",)
print(words[0])