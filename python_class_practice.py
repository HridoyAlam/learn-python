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
# the expression x + y is translated into x.__add__(y)
#However, if x hasn't implemented __add__ , and x and y are different types then y.__radd__(x) is called
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