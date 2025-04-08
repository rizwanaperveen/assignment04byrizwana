def double_numbers():
    numbers: list[int] = [15, 24, 35, 64, 80]  # Creates a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        element_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = element_at_index * 2  # Set the element at index i to be equal to the previous element times 2

    print(numbers)  # This should print the doubled list


# There is no need to edit code beyond this point

if __name__ == '__main__':
    double_numbers()