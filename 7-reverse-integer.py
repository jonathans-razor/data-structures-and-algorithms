import sys

def reverseString(x: int) -> int:
    s = str(x)
    s = s[::-1]
    s = s.lstrip('0')
    if s == '':
        return 0
    if s[-1] == '-':
        s = '-' + s[:-1]
    s = int(s)
    if s < -2**31 or s > 2**31 - 1:
        return 0
    return s

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

print(reverseString(sys.argv[1]))