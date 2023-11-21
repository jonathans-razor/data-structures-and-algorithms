import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def missingNumber(nums) -> int:
    # print("- Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.")
    return sum(range(len(nums) + 1)) - sum(nums)

inputDigits = [int(arg) for arg in sys.argv[1:]]
print(missingNumber(inputDigits))