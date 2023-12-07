import sys


def isValid(s) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Return Type: bool
    """
    stack = []  # only use append and pop
    pairs = {"{": "}", "(": ")", "[": "]"}
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
