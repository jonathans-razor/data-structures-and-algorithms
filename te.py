import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

class Solution:
    def x(s: str) -> int:
        '''
      
        Return Value:
        '''
        return

if __name__ == '__main__':
    nums = list(map(int, sys.argv[1].split(','))) if sys.argv[1] else []
    #target = int(sys.argv[2])
    solution = Solution()
    print(solution.x(nums))
