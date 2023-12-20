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
        return [["Q"]]


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(int(sys.argv[1])))
