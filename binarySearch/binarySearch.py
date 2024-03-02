from typing import List

def binarySearch(arr: List[int], tar: int) -> int:
    i, j = 0, len(arr) - 1

    while i <= j:
        mid = (i+j) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            i = mid + 1
        else:
            j = mid - 1
    return -1

if __name__ == '__main__':
    target = 5
    array = [1,2,3,4,5,6,7,8,9]
    print(binarySearch(arr=array, tar=target))