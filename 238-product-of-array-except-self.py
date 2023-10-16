import sys


class Solution:
  """
  A class that provides a method for finding the product of all elements of an array except for a given element.
  """

  def product_except_self(self, nums):
    """
    Returns an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    Args:
      nums: A list of integers.

    Returns:
      A list of integers, where answer[i] is equal to the product of all the elements of nums except nums[i].
    """

    prefix_product = [1] * len(nums)
    suffix_product = [1] * len(nums)

    for i in range(1, len(nums)):
      prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
    for i in reversed(range(len(nums) - 1)):
      suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

    answer = []
    for i in range(len(nums)):
      answer.append(prefix_product[i] * suffix_product[i])

    return answer

def main():
  """
  Reads the input array nums from the command line and prints the output array answer to the console.
  """

  nums = list(map(int, sys.argv[1:]))
  solution = Solution()
  answer = solution.product_except_self(nums)
  print(answer)

if __name__ == '__main__':
  main()