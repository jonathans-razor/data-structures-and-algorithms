import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

class Solution:
    def trap(self, heights) -> int:
      '''
      Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
      Return Value: int
      '''
      if not heights:
        return 0
      n = len(heights)  
      left = 0
      right = n - 1
      left_max = heights[left]
      print("left_max = {}".format(left_max))
      right_max = heights[right]
      print("right_max = {}".format(right_max))
      water = 0
      while left < right:
        if heights[left] < heights[right]:
          left_max = max(left_max, heights[left])
          water += left_max - heights[left]
          left += 1
        else:
          right_max = max(right_max, heights[right])
          water += right_max - heights[right]
          right -= 1
      return water

if __name__ == '__main__':
    heights = list(map(int, sys.argv[1].split(','))) if sys.argv[1] else []
    solution = Solution()
    print("Input: heights = {}".format(heights))
    print(solution.trap(heights))