import random

print("Enter a number which guess by computer!")

user_guess = int(input("Enter a number between 1 to 10"))

computer_guess = random.randint(1,10)

print(computer_guess)

while True:
    feedback = input("is this right choice? (big/small/right)")
    if feedback == "right":
        print("congratulations, you guess right choice")
        break

    elif feedback == "big" :
        print("the number you choose is big")
    elif feedback == "small":
        print("the number you choose is small")
    else:
        print("Please enter a valid number!")
        continue
    print("Enter a number which guess by computer!")

user_guess = int(input("Enter a number between 1 to 10"))
computer_guess = random.randint(1,10)

print(computer_guess)