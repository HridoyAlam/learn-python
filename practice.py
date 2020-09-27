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
'''
##tuples (immutable)
words = ("span", "eggs", "sausages",)
print(words[0])
'''
'''
#List slice

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(squares[2:6]) #like range (i : j) from i to j-1 
print(squares[3:8])
print(squares[0:1])
print(squares[0:1])
print(squares[0:1])
'''
'''
#if the first number is omited in a slice, it is taken to be the start of the list
#if the second number is omited, it is taken to be end

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[ :7])
print(squares[7:])
print(squares[ : : 2]) #first to last with step 2 
print(squares[2 : 8 : 3 ]) # 2nd index to  to (8-1)index with step 3
'''
'''
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
for i in range(2,8,3):
    print(squares[i])

print(squares[1 : -1]) # first to end-1

#count from the end
print(squares[7 : 5 :1])# 49,36
'''
'''
#list comprehension
cubes = [ i**3 for i in range(5)]
print(cubes)

even = [i*2 for i in range(11)]
print(even)

evens =[i**2 for i in range(11) if i**2 % 2 == 0]
print(evens)
a =[i for i in range(20) if i%3 ==0]
print(a)
'''
'''
#string formatting
nums = [4,5,6]
msg = "number:{0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
# Each argument of the format functions is placed in the string at the correspoding position, 
# which is determinded using the curly braces{}
print( "{0}{1}{0}".format( "abra", "cad") )

a = "{x} , {y}".format( x= 5, y=12)
print(a)

str = "{c},{b},{a}".format(a = 5, b=9, c=7)
print(str)
'''
'''
print(", ".join(["hello", "python", "world"])) #join a list string with another string as a separtor

print("hello me".replace("me", "world")) #replace one substring a string with another
print("hello me".replace( " , ", "me"))
print("this is a sentence.".startswith("this")) #True
print("this is a sentence.".endswith("sentence."))  #true

print("this is sentence".upper())
print("THIS IS SENTENCE".lower())

print("hello, python, world".split(", "))
'''
'''
num = [55, 44, 33, 22, 11]
if all([i>5 for i in num]):
    print("all larger than 5")

if any([i % 2 == 0 for i in num]):
    print("at least one is even")

#all and any take an list as an argument, and return true if all or any(repectively)
#of their arguments evalute to True( and false otherwise)

for v in enumerate(num):
    print(v)
#the functions enumerate can be used to iterate through the values and indices of a list simultaneously

'''
'''
filename = input("enter a file name: ")

with open(filename) as f:
    text = f.read()

print(text)
'''
'''
def count_char(text, char):
    count = 0
    for i in text:
        if i == char:
            count = count + 1
    return count

file_name = input("Enter a file name: ")
with open(file_name) as f:
    text = f.read()

print(count_char(text, "r"))
'''
'''
def count_char(text, char):
    count = 0
    for i in text:
        if i == char:
            count +=1
    return count


filename = input("Enter a file name: ")

with open(filename) as f:
    text = f.read()

for i in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, i) / len(text)
    print("{0} - {1}%".format(i, round(perc,2)))


'''
'''
nums = (55,44,33,22)
print(nums[:2])

'''
# Reducing the number of times the function is called meoization
# high order functions take other functions as arguments, or return them as a results
'''
def apply_twice(fucnc, arg):
    return fucnc(fucnc(arg)) #its another fucntion as its argument, and call it twice inside its body

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))


def test(func,arg):
    return func(func(arg))
def mult(x):
    return x * x
print(test(mult, 2))

#pure functions have no side effects, and return a value that depends only on their arguments

#pure functions
def pure_functions(x, y):
    temp = x + 2 * y
    return temp /(2*x + y)

#impure Functions

some_list = []
def impure(arg):
    some_list.append(arg)
# because it change the state of some_list
'''
'''
# lambdas

def my_func(f, arg):
    return f(arg)
def mult(x):
    return 2*x*x
print(my_func(lambda x: 2*x*x,5))
print(my_func(mult,5))
'''
'''
def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2*x*x,5)) #anonymous

#named functions
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambdas
print((lambda x:x**2 + 5*x +4) (-4))
a = (lambda x: x*x)(8)
print(a)

double = lambda x: x*2
print(double(7))

triple = lambda x: x*3
add = lambda x,y: x+y

print(add(triple(3),4))


#The function map takes a function and an iterable as an arguments,
#and returns a new iterable with the function applied to each argument
def add_five(x):
    return x+5
add_five=lambda x: x +5
nums = [11, 22, 33, 44, 55]
result =list(map(add_five,nums))
print(result)

#or

add_five=lambda x: x +5
nums = [11, 22, 33, 44, 55]
result =list(map(add_five,nums))
print(result)
#or
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)

#the function filters an iterable by removing items that don't match a predicate
#(a function that returns a Boolean)
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2 == 0,nums))
print(res)


##Generators
# yield statement is used for define generator

def count_down():
    i = 5
    while i > 0:
        yield i
        i -= 1
for i in count_down():
    print(i)

# generate prime number using generator

def get_prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num +=1

# generate list using generator

def get_list(x):
    for i in range(x):
        if i % 2==0:
            yield i

print(list(get_list(11)))
'''
'''
# decorators

def decor(func):
    def wrap():
        print("========")
        func()
        print("========")
    return 
def print_text():
    print("hello world")

#decorated = decor(print_text)
#decorated()

#print_text = decor(print_text)
#print(print_text)
@decor
def print_text():
    print("hello wolrd")
'''
'''
#Sets
# sets are similar to list or dictionaraies
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs","sausage"])
print( 3 in num_set)
print("spam" not in word_set)

# to create empty set use set(), as {} creates an empty dictionaries
# sets are unordered, which means that they can't indexed
#they can not contain duplicate elements
# instead of using appennd to add to a set, use add
#the method remove removes a specific elemnet from a set: pop removes an arbitary element

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)

nums.add(-7)
print(nums)

nums.remove(3)
print(nums)

# The union operator | combines two sets to from a new one containing items in either
# the intersection operator & get items only in both
#the differences operator - gets items in the first set but not in the scond
#the symmetric difference operator ^ gets items in either set, but not both

first = {1, 2, 3, 4, 5, 6}
second ={4, 5, 6, 7, 8, 9}
print( first | second )
print( first & second )
print( first - second )
print( second - first )
print( first ^ second )

'''
'''
            ######## when to use a dictionary  #######
    -- when you need a logical association between a key:value pair
    -- when you need fast look up for your data, based on custom key
    -- when your data is being constantly modified. Remember dictionaries are mutable

            ######## When to use the other types  #######
    -- use list if you have a collection of data that does not need random access. 
    -- try to choose list when you need a simple, iterable collection that is modified frequently

    -- use a set if you need uniqueness for the elements

    -- use the tuples when your data cannot change

    #-- many times, a tuples is used in combination with a dictionary, for example
     --, a tuple migth represnt a key, beacuse it's immutable

'''
'''
                          #itertools
        #the fucntion count counts up infinitely from a value
        #the function cycle infintelty iterates through an iterable (for instacne a list or string)
        # the funtion repeat an object, either infinitley or a specific number of times

        #takewhile - takes items from an iterable while predicate functions remains true
        # chain - combines several iterables into one long one
        # accumulate - return a running total of values in an iterable


from itertools import count, cycle, accumulate, takewhile

for i in count(3):
    print(i)
    if i>=11:
        break

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))
'''
from itertools import takewhile, product, permutations
nums = [2,4,14,12,7,9,8,10]
a = (takewhile(lambda x: x%2 == 0, nums))
print(list(a))

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

a ={1,2}
print(list(product(range(3),a)))