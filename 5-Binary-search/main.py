# Native search: Scans the entire list to find the target
def native_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Binary search: Uses divide and conquer to find the target efficiently
def binary_search(lst, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2  

    if lst[midpoint] == target:
        return midpoint
    elif target < lst[midpoint]:
        return binary_search(lst, target, low, midpoint - 1)
    else:
        return binary_search(lst, target, midpoint + 1, high)  

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10

    print(native_search(lst, target))  # Output: 9
    print(binary_search(lst, target))  # Output: 9
