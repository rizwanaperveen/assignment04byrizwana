import random

round = 5

def main():
    
    print("*****Welcome To The High And Low Game*****")
    print("You have 5 rounds to guess the number")
    print("The number is between 1 to 100")
    print("Good Luck!")
    print("")

    #milestone05
    #keep track of your score

    score = 0

    #milestone 04
    #play multiple rounds
    for i in range(round):
        print("Round " + str(i+1))

    #milestone 01
    #Generate number for player and computer
    player_number = random.randint(1, 100)
    computer_number = random.randint(1,100)

    #print player number
    print(f"player number is {player_number}")
    print(f"computer number is {computer_number}")

    #milestone02
    #ask player to guess the number
    choice : str = input("Enter your guess: higher or lower")

    while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ")

    higher_and_correct : bool = choice == "higher" and player_number > computer_number
    lower_and_correct : bool = choice == "lower" and player_number < computer_number

    if higher_and_correct or lower_and_correct:
        score += 1
        print("You are correct")
        print("Your score is " + str(score))
    else:
        print("You are wrong")

        print("Your score is " + str(score))



        if score == round:
            print("Wow! You played perfectly!")
        elif score > round // 2:
            print("Good job, you played really well!")
        else:
            print("Better luck next time!")

        print("")
    print("*****Thanks for Playing!*****")

if __name__ == "__main__":
    main()