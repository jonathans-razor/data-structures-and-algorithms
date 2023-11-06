import sys

class Solution:
    def addTwoNumbers(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    solution = Solution()
    print (solution.addTwoNumbers(int(sys.argv[1]), int(sys.argv[2])))