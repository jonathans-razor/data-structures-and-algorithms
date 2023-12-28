import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
        By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
        "123"
        "132"
        "213"
        "231"
        "312"
        "321"
        Given n and k, return the kth permutation sequence.
        return value: str
        """
        if n == 1:
            return "1"
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[i-1] * i)
        result = ""
        nums = [str(i) for i in range(1, n+1)]
        for i in range(n-1, -1, -1):
            num = (k-1) // factorial[i]
            result += nums[num]
            nums.remove(nums[num])
            k = k % factorial[i]
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(int(sys.argv[1]), int(sys.argv[2])))