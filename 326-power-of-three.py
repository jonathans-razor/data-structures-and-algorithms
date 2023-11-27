import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Return Value: bool
"""
def isPowerOfThree(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return isPowerOfThree(n / 3)

print(isPowerOfThree(sys.argv[1]))