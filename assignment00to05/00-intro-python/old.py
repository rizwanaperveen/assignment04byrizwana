def main():
    anton_age : int = 21  # Anton's age is given as 21 years old
    beth_age : int = 6 + anton_age  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen_age : int = 20 + beth_age  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew_age  : int= chen_age + anton_age  # Drew is as old as Chen's age plus Anton's age,
    ethan_age : int = chen_age  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

   # Print out all of the ages!
    print(f"Anton is {anton_age} yeas old")
    print(f"Beth is {beth_age} years old")
    print(f"Chen is {chen_age} years old")
    print(f"Drew is {drew_age} years old")
    print(f"Ethan is {ethan_age} years old")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()