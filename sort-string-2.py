import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

class Solution:
    def sortString(self, s: str) -> str:
        """
        return value: bool
        """
        sortedString = "".join(sorted(s))
        if sortedString == s:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortString(sys.argv[1]))