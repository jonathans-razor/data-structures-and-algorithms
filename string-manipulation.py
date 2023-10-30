import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def stringManipulation(s: str) -> str:
    print('       input string: ' + s)
    print('    first character: ' + s[0])
    lengthOfString = len(s)
    halfString = lengthOfString // 2
    print('         halfString: ' + str(halfString))
    middleString = s[halfString - 1:halfString + 2]
    print('middle 3 characters: ' + middleString)
    print('     last character: ' + s[-1])
    return s

stringManipulation(sys.argv[1])