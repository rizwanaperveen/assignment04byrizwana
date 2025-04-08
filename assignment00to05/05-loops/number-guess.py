import random

def main():
    
    secret_number = random.randint(1, 99)
    print("I imagine a number around 1 to 99.")

# Get user's guess
    user_guess = int(input("Enter your guess: "))
    # True if guess is not equal to secret number
    while user_guess != secret_number:
        if user_guess < secret_number:  # If-statement is True if guess is less than secret number
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() # Print an empty line to tidy up the console for new guesses
        user_guess = int(input("Enter a new guess: "))  # Get a new guess from the user
        
    print("Congrats! The number was: " + str(secret_number))


if __name__ == '__main__':   
    main()