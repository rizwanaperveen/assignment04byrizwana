import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100

def random_numbers():
    return [random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER) for _ in range(10)]

print(random_numbers())
