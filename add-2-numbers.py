import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

class Solution:
    def addTwoNumbers(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    solution = Solution()
    print (solution.addTwoNumbers(int(sys.argv[1]), int(sys.argv[2])))