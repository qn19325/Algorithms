"""Module providing a function for finding the First Occurence of an Element."""
from typing import List

def first_occurence(arr: List[int], tar: int):
    """Function for Finding the First Occurence of an Element."""
    i, j = 0, len(arr)-1
    res = -1
    while i <= j:
        mid = (i+j) // 2
        if arr[mid] == tar:
            res = mid
            j = mid - 1
        elif arr[mid] > tar:
            j = mid - 1
        else:
            i = mid + 1
    return res


if __name__ == '__main__':
    TARGET = 6
    array = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
    print(first_occurence(arr=array, tar=TARGET))
