import sys

def raiseToThePower(x: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * raiseToThePower(x, n - 1)  

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

print(raiseToThePower(int(sys.argv[1]), int(sys.argv[2])))