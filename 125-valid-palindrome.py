import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def isValidPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(randomVariableName for randomVariableName in s if randomVariableName.isalnum())
    s2 = s[::-1]
    print(s)
    print(s2)
    if s == s2:
        return True
    return False

print(isValidPalindrome(sys.argv[1]))