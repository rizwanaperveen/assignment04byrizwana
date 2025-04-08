import colorama
import rich 

def calculate_perimeter():
    # Get the 3 side lengths of the triangle
    side1: float = float(input("Enter the length of side 1? "))
    print(colorama.Style.BRIGHT + "Side 1 is " + str(side1))
    side2: float = float(input("Enter the length of side 2? "))
    print(colorama.Style.BRIGHT + "Side 2 is " + str(side2))
    side3: float = float(input("Enter the length of side 3? "))
    print(colorama.Style.BRIGHT + "Side 3 is " + str(side3))

    # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print(colorama.Style.BRIGHT + "The perimeter of the triangle is " + str(side1 + side2 + side3))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    calculate_perimeter()