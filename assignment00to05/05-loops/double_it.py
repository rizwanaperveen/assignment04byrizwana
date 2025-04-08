#Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# Start the loop
while True:
    # Ask the user for a number
    num = float(input("Enter a number: "))

    # Double the number
    doubled = num * 2

    # Print the result
    print("Doubled value:", doubled)

    # Check if the doubled number is 100 or more
    if doubled >= 100:
        break
