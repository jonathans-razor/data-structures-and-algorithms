import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def isPowerOfTwo(n: int) -> bool:
    #print("Given an integer n, return true if it is a power of two. Otherwise, return false.")
    i = 0
    while 2**i <= n:
        if 2**i == n:
            return True
        i += 1
    return False

print(isPowerOfTwo(int(sys.argv[1])))