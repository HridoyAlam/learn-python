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