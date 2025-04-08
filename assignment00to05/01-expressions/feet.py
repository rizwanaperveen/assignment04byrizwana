#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.
feet: float = float(input("Enter the number of feet: "))
inches: float = feet * INCHES_IN_FOOT
print(f"{feet} feet is {inches} inches.")