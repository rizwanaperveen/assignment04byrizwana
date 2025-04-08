def add_numbers(numbers)-> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total_numbers: int = 0
    for number in numbers:
        total_numbers += number

    return total_numbers

#function to sum a list of numbers

def main():
    numbers: list[int] = [10, 12, 67, 48, 59]  # Make a list of numbers
    sum_of_numbers: int = add_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()