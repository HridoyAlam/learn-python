import random

for i in range(3):
    print(random.randint(10,15))

#random name picker

club = ['ac','apc','bsc','cdc','yes','yef']
leader = random.choice(club)
print(leader)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice = Dice()
print(dice.roll())