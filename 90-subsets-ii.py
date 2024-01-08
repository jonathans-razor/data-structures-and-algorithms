import sys
import argparse

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)


class Solution:
    def subsetsWithDup(self, nums):
        """
        Given an integer array nums that may contain duplicates, return all possible
        subsets
        (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.

        Example 1:

        Input: nums = [1,2,2]
        Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        Example 2:

        Input: nums = [0]
        Output: [[],[0]]

        Constraints:

        1 <= nums.length <= 10
        -10 <= nums[i] <= 10
        return value: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LeetCode problem number 90 solution")
    parser.add_argument(
        "nums", metavar="N", type=int, nargs="+", help="an integer list"
    )
    args = parser.parse_args()
    solution = Solution()
    print(solution.subsetsWithDup(args.nums))
