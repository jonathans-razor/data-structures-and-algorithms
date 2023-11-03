import sys

def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s
    res = ""
    for row in range(numRows):
        increment = 2 * (numRows - 1)
        for i in range(row, len(s), increment):
            # This applies to the first and last row.
            res += s[i]
            # This applies to the middle rows.
            if row != 0 and row != numRows - 1 and i + increment - 2 * row < len(s):
                res += s[i + increment - 2 * row]
    return res

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

print(convert(sys.argv[1], int(sys.argv[2])))