class Point:
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Moving")
    
    def draw(self):
        print("Drawing")

class Persons:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi!, I am {self.name}")

class Mamal:
    def walk(self):
        print("walk")


class Dog(Mamal):
    def bark(self):
        print("Bark!!!!!")
    

class Cat(Mamal):
    def be_annoying(self):
        print("meoeoeooe")


d1 = Dog()
d1.walk()
d1.bark()
#john =Persons('Johan smith')
#john.talk()
#points = Point(10,20)
#print(points.x, points.y)