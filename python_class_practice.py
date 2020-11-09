'''
class Animal:

    def __init__(self,name,color):
        self.color = color
        self.name = name

class Cat(Animal):
    def purr(self):
        print("purr...")

class Dog(Animal):
    def bark(self):
        print("woof!")


felix = Cat("fido", "ref")
print(felix.color)
felix.purr()
'''
'''
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()
...

Magic method are special methods which have double underscore at the begining and end of their names.
They are also known as dunders exp. ___init__
They are used to create functionality that can't be represented as a normal method
One common use of them is operator overloading
'''
# More Magic Method
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |
# __It__ for <
# __Ie__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=
#there are seveal magic method for making classes act like container
# __len__ for len() 
# __getitem__ for  indexing
# __setitem__ for assigning to indexed values
# __delitem__ for delelting indexed values
# __iter__ for iteration over objects
# __contains__ for in
# __call__ for calling objects as functions
# __str__ for 


# the expression x + y is translated into x.__add__(y)
#However, if x hasn't implemented __add__ , and x and y are different types then y.__radd__(x) is called
# if __ne__ is not implemented, it returns the opposite of __eq__
'''
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other): #the __add__ method allow for the defination of a custom behavior for the + operator in class
        return Vector2D(self.x + other.x, self.y+ other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
'''
'''
class specialString:
    def __init__(self, cont):
        self.cont = cont
    
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
    
    def __gt__(self, other):
        for index in range( len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result +=">" + other.cont[index:]
            print(result)    
spam = specialString("spam")
hello = specialString("Hello world")
eggs = specialString("eggs")
spam > eggs
print(spam/hello)
'''
'''
import random
class VagueList:
    def __init__(self, cont):
        self.cont = cont
    
    def __getitem__(self, index):
        return self.cont[ index + random.randint(-1,1) ]
    
    def __len__(self):
        return random.randint(0, len(self.cont) * 2 )

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
'''
class Queue:
    def __init__(self, content):
        self._hiddenlist =list(content)
    
    def push(self,value):
        self._hiddenlist.insert(0, value)
    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue ({})".format(self._hiddenlist)
    
queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)