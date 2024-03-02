from typing import List

def firstTrue(arr: List[bool]) -> int:
    i, j = 0, len(arr)-1
    res = -1
    while i <= j:
        mid = (i+j) // 2
        if arr[mid] == False:
            i = mid + 1
        else:
            res = mid
            j = mid - 1
    return res

if __name__ == '__main__':
    arr = [False, False, True, True, True]
    print(firstTrue(arr))
