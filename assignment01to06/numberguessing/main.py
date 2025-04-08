import random
x = random.randint(1, 10)

y = ""
attempt = 0
try:
    while x != y:
        y = int(input("Enter a number from 1 to 10: "))
        attempt += 1
        if x == y:
         print("You win!")
         print(f"Attempts are taken by you: {attempt}")
        elif x > y:
            print("You choose too small number!")
        elif x < y:
            print("You choose too large number!")
except:
    print("Please enter a number from 1 to 10")
