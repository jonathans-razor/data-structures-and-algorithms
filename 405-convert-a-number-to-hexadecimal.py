import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

"""
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

Return Value: string
"""
def toHex(num: int) -> str:
    if num == 0:
        return "0"
    if num < 0:
        num += 2**32
    hexadecimal = "0123456789abcdef"
    result = ""
    while num > 0:
        result += hexadecimal[num % 16]
        num //= 16  
    return result[::-1]

print(toHex(int(sys.argv[1])))