import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def convertToTitle(columnNumber: int) -> str:
    result = ""
    while columnNumber > 0:
        columnNumber -= 1
        result = chr(65 + columnNumber % 26) + result
        columnNumber //= 26
    return result

print(convertToTitle(int(sys.argv[1])))