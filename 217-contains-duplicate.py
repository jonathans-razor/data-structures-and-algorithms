import argparse

def hasDuplicates(nums):
    return len(nums) != len(set(nums))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if an array has duplicates.')
    parser.add_argument('arr', metavar='N', type=int, nargs='+',
                        help='an integer array')
    args = parser.parse_args()
    if hasDuplicates(args.arr):
        print('The array contains duplicates.')
    else:
        print('The array does NOT contain duplicates.')