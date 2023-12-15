import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """

        Return Value:
        """
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch(sys.argv[1], sys.argv[2]))