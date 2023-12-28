import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)


class Solution:
    def factorialize_3(self, n: int) -> int:
        """
        Doesn't use recursion.
        return value:
        lu: Dec-28-2023
        """
        myFactorial = 1
        for i in range(1, n + 1):
            myFactorial = myFactorial * i
        return myFactorial


if __name__ == "__main__":
    solution = Solution()
    print(solution.factorialize_3(int(sys.argv[1])))