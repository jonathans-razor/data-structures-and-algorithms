import sys
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()

if __name__ == "__main__":
    # Parse command line arguments
    args = sys.argv[1:]
    nums1 = list(map(int, args[0].split(",")))
    m = int(args[1])
    nums2 = list(map(int, args[2].split(",")))
    n = int(args[3])

    # Create solution object
    sol = Solution()

    # Call merge method
    sol.merge(nums1, m, nums2, n)

    # Print result
    print(nums1)