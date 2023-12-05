import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Return Value: str
"""
def intToRoman(num: int) -> str:
    roman = ""
    if num >= 1000:
        roman += "M" * (num // 1000)
        num %= 1000
    if num >= 900:
        roman += "CM"
        num %= 900
    if num >= 500:
        roman += "D"
        num %= 500
    if num >= 400:
        roman += "CD"
        num %= 400
    if num >= 100:
        roman += "C" * (num // 100)
        num %= 100
    if num >= 90:
        roman += "XC"
        num %= 90
    if num >= 50:
        roman += "L"
        num %= 50
    if num >= 40:
        roman += "XL"
        num %= 40
    if num >= 10:
        roman += "X" * (num // 10)
        num %= 10
    if num >= 9:
        roman += "IX"
        num %= 9
    if num >= 5:
        roman += "V"
        num %= 5
    if num >= 4:
        roman += "IV"
        num %= 4
    if num >= 1:
        roman += "I" * num
    return roman

print(intToRoman(int(sys.argv[1])))