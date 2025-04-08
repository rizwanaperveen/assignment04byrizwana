import random

DONE_LIKELIHOOD = 0.3

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the computer show up at work late? It had a hard drive.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why can't your nose be 12 inches long? Because then it would be a foot.",
    "How does a penguin build its house? Igloos it together.",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kat ads.",
    "Why did the math book look sad? It had too many problems.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "What do you call fake spaghetti? An impasta!"
]

def chaotic_jokes():
    for joke in jokes:
        if done():
            return
        print(joke)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to tell you some jokes... unless I suddenly lose interest.")
    chaotic_jokes()
    print("That's all I've got!")

if __name__ == "__main__":
    main()
