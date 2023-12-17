import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

class Solution:
    def permute(self, nums):
        """
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
        Return Value: -> List[int]
        """
        # Recursive
        # Time Complexity: O(n*n!)
        # Space Complexity: O(n*n!)
        def permuteRecursive(nums, start, end, result):
            if start == end:
                result.append(nums.copy())
            else:
                for i in range(start, end + 1):
                    nums[start], nums[i] = nums[i], nums[start]
                    permuteRecursive(nums, start + 1, end, result)
                    nums[start], nums[i] = nums[i], nums[start]

        result = []
        permuteRecursive(nums, 0, len(nums) - 1, result)
        return result

if __name__ == "__main__":
    nums = list(map(int, sys.argv[1].split(","))) if sys.argv[1] else []
    solution = Solution()
    print(solution.permute(nums))