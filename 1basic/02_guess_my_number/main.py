import random
def secret_number():
    my_number = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100.")

    while True:
        guess_number = int(input("Take a guess: "))
        if guess_number == my_number:
            print("*******Good job! You guessed my number!********")
            break
        elif guess_number > my_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

secret_number()