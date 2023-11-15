import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def majorityElement(nums) -> int:
    nums.sort()
    n = len(nums)
    return nums[n // 2]

# Example usage: python plus_one.py 1 2 3
input_digits = [int(arg) for arg in sys.argv[1:]]
print(majorityElement(input_digits))