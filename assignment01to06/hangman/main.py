import random
words = ["HTML", "CSS", "JAVA", "PYTHON", "C++"]

word = random.choice(words)

guess_letters = []

attempts = 6

print("Welcome To Hangman Game")
print("_", len(word))

while attempts > 0:
    guess = input("\n guess the letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("write one alphabet only")
        continue
    if guess in guess_letters:
        print("This letter is already guess, choose another letter")
        continue
    guess_letters.append(guess)

    if guess in word:
       print("Correct guess")
    else:
        attempts -= 1
        print(f"wrong {attempts} attempts")

    displayed_word = " ".join([letter if letter in guess_letters else "_" for letter in word])
    print(displayed_word)

    if "_" not in displayed_word:
        print(f"Congratulations! the correct word is : {word}")
        break
else:
    print(f"Game over! 'The correct word is {word}'")