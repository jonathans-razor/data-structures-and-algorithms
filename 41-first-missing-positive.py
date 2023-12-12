import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

class Solution:
    def firstMissingPositive(self, nums) -> int:
      '''
      Given an unsorted integer array nums, return the smallest missing positive integer.
      You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

      Return Value: int
      '''
      if not nums:
        return 1

      def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

      n = len(nums)
      for i in range(n):
        while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
          swap(nums, i, nums[i] - 1)

      for i in range(n):
        if nums[i] != i + 1:
          return i + 1

      return n + 1

if __name__ == '__main__':
    nums = list(map(int, sys.argv[1].split(','))) if sys.argv[1] else []
    solution = Solution()
    print(nums)
    print(solution.firstMissingPositive(nums))

    '''
    I understood this code but it exceeded the time limit:

      if not nums:
        return 1
      max_num = max(nums)
      if max_num <= 0:
        return 1
      for i in range(1, max_num + 2):
        if i not in nums:
          return i

    '''