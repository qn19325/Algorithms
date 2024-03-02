"""Module providing a function for finding the First Element Not Smaller Than Target."""
from typing import List

def first_greater_equal_target(arr: List[str], tar: str):
    """Function for Finding the First Element Not Smaller Than Target."""
    i, j = 0, len(arr)-1
    res = arr[0] # If there is not element greater than equal to target return first letter
    while i <= j:
        mid = (i+j) // 2
        if arr[mid] > tar:
            res = arr[mid]
            j = mid - 1
        else:
            i = mid + 1
    return res


if __name__ == '__main__':
    TARGET = "a"
    array = ["c","f","j"]
    print(first_greater_equal_target(arr=array, tar=TARGET))
