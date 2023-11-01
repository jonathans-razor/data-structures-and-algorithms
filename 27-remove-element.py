import argparse

def removeElement(nums, val):
  index = 0
  for i in range(len(nums)):
      if nums[i] != val:
          nums[index] = nums[i]
          index += 1
  return index, nums

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if an array has duplicates.')
    parser.add_argument('arr', metavar='N', type=int, nargs='+',
                        help='an integer array')
    args = parser.parse_args()
    val = args.arr[-1]
    print(removeElement(args.arr, val))
