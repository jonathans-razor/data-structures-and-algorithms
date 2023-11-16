import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def convertTitleToNumber(columnTitle: str) -> int:
    result = 0
    for i in range(len(columnTitle)):
        result *= 26
        result += ord(columnTitle[i]) - ord('A') + 1
    return result

print(convertTitleToNumber(sys.argv[1]))