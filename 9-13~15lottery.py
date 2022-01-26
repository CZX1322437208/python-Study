from random import randint
import random


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        self.sides = randint(1, 6)
        print(self.sides)

    def roll_die10(self):
        self.sides = randint(1, 10)
        print(self.sides)

    def roll_die20(self):
        self.sides = randint(1, 20)
        print(self.sides)


die = Die()
print(die.sides)
print("6 sides")
for i in range(0, 10):
    die.roll_die()
print("10 sides")
for i in range(0, 10):
    die.roll_die10()
print("20 sides")
for i in range(0, 10):
    die.roll_die20()

lottery = ['A', 'B', 'C', 'D', 'E', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lot = []
lot = random.sample(lottery, 4)
print("(['0', '1', 'A', 'B']为中奖号码)")
print(lot)

x = 0
while True:
    if ['0', '1', 'A', 'B'] == sorted(lot):
        print(f"循环{x}次中奖")
        break
    else:
        lot = random.sample(lottery, 4)
        x += 1
