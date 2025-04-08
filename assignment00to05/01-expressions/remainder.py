def remainder_calc():
    dividend = int(input("Enter the value of a: "))
    divisor = int(input("Enter the value of b: "))
    quotient = dividend // divisor
    remainder = dividend % divisor
    print("The result of dividend and divisor is:", quotient, "with remainder:", remainder)


remainder_calc()