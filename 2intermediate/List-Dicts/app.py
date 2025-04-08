#A function that can access specific element of list

def access_items(friends_name, index):
    try:
        return friends_name[index]
    except IndexError:
        return "Index out of range."

#A function that can modify specific element of list
def modify_items(friends_name, index, new_value):
    try:
        friends_name[index] = new_value
        return friends_name
    except IndexError:
        return "Index out of range."

#A function that can slice a list
def slice_list(friends_name, start, end):
    try:
        return friends_name[start:end]
    except IndexError:
        return "Invalid indices."

#A function that can remove an element from a list
def remove_items(friends_name, value):
    
    friends_name.remove(value)
    return friends_name
    

#A function that can append an element to a list
def append_items(friends_name, value):
    friends_name.append(value)
    return friends_name

#A function that can sort a list
def sort_list(friends_name):
    friends_name.sort()
    return friends_name

def index_game():
    friends_name = ["John", "Alice", "Bob", "Charlie", "David"]  # Example list
    print("Current list:", friends_name)

    print("Choose an operation: access, modify, slice, remove, append, sort")

    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_items(friends_name, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_items(friends_name, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(friends_name, start, end))
    elif operation == "remove":
        value = input("Enter value to remove: ")
        print(remove_items(friends_name, value))
    elif operation == "append":
        value = input("Enter value to append: ")
        print(append_items(friends_name, value))
    elif operation == "sort":
        print(sort_list(friends_name))
    else:
        print("Invalid operation.")

index_game()
