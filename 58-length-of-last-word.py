import sys


def lengthOfLastWord(s: str) -> int:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    A word is a maximal substring consisting of non-space characters only.
    return value: int
    """
    if len(s) == 0:
        return 0
    words = s.split()
    if len(words) == 0:
        return 0
    return len(words[-1])

if __name__ == "__main__":
    print(lengthOfLastWord(sys.argv[1]))