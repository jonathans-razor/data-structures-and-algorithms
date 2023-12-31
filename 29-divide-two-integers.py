import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def divide(dividend: int, divisor: int) -> int:
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

    The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

    Return Value:
    """
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    if divisor == 1:
        return dividend
    if divisor == -1:
        return -dividend
    if dividend == divisor:
        return 1
    if dividend == 0:
        return 0
    if divisor == 0:
        return 0
    if dividend < 0 and divisor < 0:
        return divide(-dividend, -divisor)
    if dividend < 0:
        return -divide(-dividend, divisor)
    if divisor < 0:
        return -divide(dividend, -divisor)
    result = 0
    while dividend >= divisor:
        dividend -= divisor
        result += 1
    return result

print(divide(int(sys.argv[1]), int(sys.argv[2])))