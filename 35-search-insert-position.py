import argparse
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
  if target in nums:
      return nums.index(target)
  else:
      for i in range(len(nums)):
          if nums[i] > target:
              return i
      return len(nums)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Return the index if the target is found. If not, return the index here it would be if it were inserted in order.")
    parser.add_argument("nums", metavar="N", type=int, nargs="+", help="an integer array")
    parser.add_argument("target", metavar="target", type=int, help="the number to insert")
    args = parser.parse_args()
    #print(args.nums)
    #print(args.target)
    print(searchInsert(args.nums, args.target))
