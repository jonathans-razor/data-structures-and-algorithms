import sys

def factorialize(n):
    """
    Calculates the factorial of a non-negative integer.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the given number.

    Example:
    >>> factorialize(5)
    120
    """
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorialize(n - 1)

print(factorialize(int(sys.argv[1])))