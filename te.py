import sys

def reverseString(s: str) -> int:
    return s[::-1]

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

print(reverseString(sys.argv[1]))