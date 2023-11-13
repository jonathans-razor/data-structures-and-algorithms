import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    # Get input from the command line
    input_list = sys.argv[1:]

    # Convert input to a list of integers
    nums = list(map(int, input_list))

    # Call the function and print the result
    result = singleNumber(nums)
    print(result)
