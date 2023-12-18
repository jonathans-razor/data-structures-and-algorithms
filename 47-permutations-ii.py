import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)


class Solution:
    def permute(self, nums):
        """
        Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
        Return Value: -> List[int]
        """
        def backtrack(nums, path, result):
            if not nums:
                result.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i + 1 :], path + [nums[i]], result)

        result = []
        nums.sort()
        backtrack(nums, [], result)
        return result


if __name__ == "__main__":
    nums = list(map(int, sys.argv[1].split(","))) if sys.argv[1] else []
    solution = Solution()
    print(solution.permute(nums))
