import random
import string

def generated_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter your password length: "))

password = generated_password(length)
print("Your desired generated password:", password)