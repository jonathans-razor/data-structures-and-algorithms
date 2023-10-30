import sys

def stringManipulation(s: str) -> str:
    print('   input string: ' + s)
    print('first character: ' + s[0])
    print(' last character: ' + s[-1])
    return s

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

stringManipulation(sys.argv[1])