#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# Takes the length of the list and minuses 1 since they are zero-indexed (we start counting at 0)
#print(lst[len(lst) - 1])

# The line below works too!!
# print(lst[-1]) 

def get_last_element(lst):
    print(lst[-1])

get_last_element([1, 2, 3, 4, 5])

get_last_element(["a", "b", "c", "d", "e"])