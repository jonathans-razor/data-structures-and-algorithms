import sys

"""
Given a football score, return true if the score is a palindrome, false otherwise.
Return Value: boolean
"""

"""
Concatenate 2 numbers into 1.
Return Value: the concatenated numbers.
"""
def concatenate2NumbersInto1(s1, s2):
    return s1 + s2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("- Parameter(s) expected.")
        sys.exit(1)

    string1 = sys.argv[1]
    string2 = sys.argv[2]
    concatenatedString = concatenate2NumbersInto1(string1, string2)

    reversed_string = concatenatedString[::-1]

    if concatenatedString == reversed_string:
        print("True")
    else:
        print("False") 