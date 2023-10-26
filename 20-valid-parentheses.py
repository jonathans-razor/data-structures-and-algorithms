import sys

def isValid(s) -> bool:
    stack = [] # only use append and pop
    pairs = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    for encloser in s:
        if encloser in pairs:
            stack.append(encloser)
        elif len(stack) == 0 or encloser != pairs[stack.pop()]:
            return False
    return len(stack) == 0

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

string = sys.argv[1]

print(isValid(string))
