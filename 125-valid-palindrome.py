import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def r(s: str) -> int:
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    s2 = s[::-1]
    print(s)
    print(s2)
    if s == s2:
        return True
    return False

print(r(sys.argv[1]))