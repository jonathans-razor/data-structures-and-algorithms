import sys

def two_sum(nums, target):
    destination_array = {}
    for i, num in enumerate(nums):
      #print(i, num)
      if target - num in destination_array:
        return [destination_array[target - num], i]
      destination_array[num] = i

if __name__ == "__main__":
    nums = list(map(int, sys.argv[1:-1]))
    target = int(sys.argv[-1])
    print(two_sum(nums, target))