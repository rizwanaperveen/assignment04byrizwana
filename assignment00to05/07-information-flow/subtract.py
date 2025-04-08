def main():
    num1 = int(input("Enter a number: "))
    result = subtract_integer(num1)
    print("This should be zero:", result)

def subtract_integer(num):
    """
    Subtracts the number from itself and returns the result (should always be zero).
    """
    return num - num

if __name__ == '__main__':
    main()
