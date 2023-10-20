import sys

def longest_consecutive_sequence(nums):
    i = 0
    max_len, cur_max_len = 1, 1
    nums = list(set(nums))
    nums.sort()
    while i < len(nums) - 1:
        if nums[i + 1] - nums[i] == 1:
            cur_max_len += 1
        else:
            cur_max_len = 1
        i += 1
        if cur_max_len > max_len:
            max_len = cur_max_len
    return max_len if nums != [] else 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n- Parameter(s) expected.")
        exit(1)

    print(sys.argv[1:])
    print('- Longest consecutive sequence.')
    nums = list(map(int, sys.argv[1].split()))
    print(longest_consecutive_sequence(nums))
