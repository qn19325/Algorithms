"""Module providing a function for Estimating the Square Root of an Integer."""

def sqrt_est(integer: int):
    """Function for Estimating the Square Root of an Integer."""
    i, j = 0, integer
    while i <= j:
        mid = (i+j) // 2
        sqr = (mid)**2
        if sqr == integer:
            return mid
        elif sqr > integer:
            j = mid - 1
        else:
            i = mid + 1
    return (i+j) // 2



if __name__ == '__main__':
    INPUT = 64
    print(sqrt_est(integer=INPUT))
