import random

NUM_ROUNDS = 5  # Number of rounds in the game

def play_round():
    """Plays a single round of the High-Low Game and returns 1 if the player wins, otherwise 0."""
    computer_num = random.randint(1, 100)
    your_num = random.randint(1, 100)
    
    print(f"\nYour number is {your_num}")
    choice = input("Do you think your number is higher or lower than the computer's? ").strip().lower()

    # Ensure valid input
    while choice not in ["higher", "lower"]:
        choice = input("Invalid choice! Please enter 'higher' or 'lower': ").strip().lower()

    if your_num == computer_num:
        print(f"It's a tie! Both numbers are {your_num}. No points this round.")
        return 0

    if (choice == "higher" and your_num > computer_num) or (choice == "lower" and your_num < computer_num):
        print(f"You were right! The computer's number was {computer_num}.")
        return 1
    else:
        print(f"Wrong guess! The computer's number was {computer_num}.")
        return 0

def main():
    print("Welcome to the High-Low Game!")
    print('-' * 40)

    while True:
        your_score = sum(play_round() for _ in range(NUM_ROUNDS))
        print(f"\nYour final score is {your_score}/{NUM_ROUNDS}.")

        if your_score == NUM_ROUNDS:
            print("Wow! You played perfectly!")
        elif your_score > NUM_ROUNDS // 2:
            print("Good job, you played really well!")
        else:
            print("Better luck next time!")

        # Ask if the player wants to play again
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
