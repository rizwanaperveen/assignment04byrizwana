def double_number():
    curr_value = int(input("Enter a number: "))
    
    while curr_value < 200:
        curr_value = curr_value * 2
        print(curr_value)
    print("The value has reached or exeed 200.")


double_number()