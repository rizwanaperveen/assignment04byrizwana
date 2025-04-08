import random

contexts = {
    0: [
        "I accidentally sat on a {} yesterday. It was not pleasant.",
        "Have you ever seen a {} ride a skateboard? Now you have.",
        "In my dreams, I'm always being chased by a giant {}.",
    ],
    1: [
        "Sometimes I like to {} in the rain just to feel alive.",
        "Never try to {} while holding hot soup. Trust me.",
        "If you {} three times fast, you unlock a secret level in life.",
    ],
    2: [
        "The moon looked so {} last night, I almost took a bite out of it.",
        "I painted my entire house {} just to confuse my neighbors.",
        "Feeling {} is just part of the human experience.",
    ]
}

def make_silly_sentence(word, part_of_speech):
    if part_of_speech in contexts:
        sentence_template = random.choice(contexts[part_of_speech])
        print(sentence_template.format(word))
    else:
        print("Oops! Part of speech must be 0 (noun), 1 (verb), or 2 (adjective).")

def main():
    word = input("Enter a word (noun, verb, or adjective): ")
    print("What part of speech is it?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_silly_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
