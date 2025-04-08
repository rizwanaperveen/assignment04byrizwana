prompt : str = "What do you want?"

joke : str = "Here is a joke for you! SophHereia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'."

sorry : str = " Sorry,I only tell jokes."

def main():
    user_input = input(prompt).strip().lower()

    if user_input == "joke":
        print(joke)
    else:
        print(sorry)
if __name__ ==  "__main__":
    main()















