MINIMUM_HEIGHT : int = 30 # arbitrary units :)

def tall_enough_to_ride():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    tall_enough_to_ride()