"""
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.

"""
print("*****Dicesimulator*****_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
import  random

Number_Sides = 6
def roll_dice():
    """
    Simulates rolling two dice and prints their total

    """
    die1: int = random.randint(1, Number_Sides)
    die2: int = random.randint(1, Number_Sides)
    total: int = die1 + die2
   
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))


if __name__ == '__main__':
    main()