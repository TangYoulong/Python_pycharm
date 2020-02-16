from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1,self.sides)
        print(x)
die6 = Die(6)
for i in range(1,10):
    die6.roll_die()
    i += 1
