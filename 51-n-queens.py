import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)


class Solution:
    def solveNQueens(self, n: int):
        """
        The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

        Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

        Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
        return value: List[List[str]]
        """
        def dp(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    dp(queens + [q], xy_diff + [p - q], xy_sum + [p + q])
        result = []
        dp([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]

if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(int(sys.argv[1])))