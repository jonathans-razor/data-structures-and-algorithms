import sys

class Solution:
    def searchRange(self, nums, target: int):
        """
        Given an array of integers nums sorted in non-decreasing order, find the starting and ending position a given target value.

        If target is not found in the array, return [-1, -1].

        You must write an algorithm with O(log n) runtime complexity.
                inputs: nums: List[int], target: int
                return value: [left, right]
        """
        if not nums:
            return [-1, -1]

        def search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = search_left(nums, target)
        right = search_right(nums, target)

        if left <= right:
            return [left, right]
        else:
            return [-1, -1]

if __name__ == '__main__':
    nums = list(map(int, sys.argv[1].split(','))) if sys.argv[1] else []
    target = int(sys.argv[2])
    solution = Solution()
    print(solution.searchRange(nums, target))