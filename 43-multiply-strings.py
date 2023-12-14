import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

        Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.      
        Return Value:
        '''
        # 1. Convert the strings to integers

        # 2. Multiply the integers
        # 3. Convert the result back to string
        # 4. Return the result
        return

if __name__ == '__main__':
    nums = list(map(int, sys.argv[1].split(','))) if sys.argv[1] else []
    #target = int(sys.argv[2])
    solution = Solution()
    print(solution.x(nums))
