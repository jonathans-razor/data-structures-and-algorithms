import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two attack each other.
        Given an integer n, return the number of distinct solutions to the n-queens puzzle.
        return value: int
        """
        def dp(queens, xy_diff, xy_sum):
            row = len(queens)
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in queens or row - col in xy_diff or row + col in xy_sum:
                    continue
                count += dp(queens + [col], xy_diff + [row - col], xy_sum + [row + col])
            return count
        return dp([], [], [])

if __name__ == "__main__":
    nums = list(map(int, sys.argv[1].split(","))) if sys.argv[1] else []
    # target = int(sys.argv[2])
    solution = Solution()
    print(solution.totalNQueens(int(sys.argv[1])))