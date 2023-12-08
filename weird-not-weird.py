import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def weirdNotWeird(n: int):
    """
    Given an integer, , perform the following conditional actions:

    If  is odd, print Weird
    If  is even and in the inclusive range of  to , print Not Weird
    If  is even and in the inclusive range of  to , print Weird
    If  is even and greater than , print Not Weird
    Input Format
    A single line containing a positive integer, 
    Retrun Value: str
    """
    if n % 2 != 0:
        return "Weird"
    if n == 2:
        return "Not Weird"
    if n == 4:
        return "Not Weird"
    if n >= 6 and n <= 20:
        return "Weird"
    return "Not Weird"

print(weirdNotWeird(int(sys.argv[1])))