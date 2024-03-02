"""Module providing a function for Finding the First True in a Sorted Boolean Array."""
from typing import List

def first_true(arr: List[bool]) -> int:
    """Function for Finding the First True in a Sorted Boolean Array."""
    i, j = 0, len(arr)-1
    res = -1
    while i <= j:
        mid = (i+j) // 2
        if arr[mid] is False:
            i = mid + 1
        else:
            res = mid
            j = mid - 1
    return res

if __name__ == '__main__':
    array = [False, False, True, True, True]
    print(first_true(arr=array))
