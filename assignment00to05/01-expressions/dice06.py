#Simulate rolling two dice, and prints results of each roll as well as the total.
import random

Number_Sides = 6

def roll_dice():
    die1 = random.randint(1, Number_Sides)
    print("Die 1:", die1)
    die2 = random.randint(1, Number_Sides)
    print("Die 2:", die2)
    total = die1 + die2
    print("Total of two dice:", total)
if __name__ == '__main__':
    roll_dice()
    roll_dice()
    roll_dice()