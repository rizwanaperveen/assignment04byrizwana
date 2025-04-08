import random
import time

#implmentation of binary search algorithm

#we will prove that binary search is more efficient than native search

#native search : scan entire list and ask if its equal to target

# if yes, return index

# if no, return -1

def native_search(list, target):
    #example list = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

# binary search uses divide and conquer!
# we will halve the list each time we search

def binary_search(list, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1
    #example list = [1,2,3,4,5,6,7,8,9,10]
    
    midpoint = (low + high) // 2     #2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint - 1)
    else:
        return binary_search(list, target, midpoint + 1, high)
if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9,10]
    target = 10

    print(native_search(list, target))
    print(binary_search(list, target))# Native search: Scans the entire list to find the target

    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))
    start = time.time()
    for target in sorted_list:
        native_search(sorted_list, target)

    end = time.time()
    print("Native Search Time:", (end - start)/length, "seconds")