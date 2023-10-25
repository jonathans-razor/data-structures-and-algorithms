import argparse

def twoSum(nums, target):
    for i in range(len(nums)):
        print("i: " +str(i))
        for j in range(i+1, len(nums)):
            print("j: " + str(j))
            if nums[i] + nums[j] == target:
                arr = []
                arr.append(i)
                arr.append(j)
                return arr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if an array has duplicates.')
    parser.add_argument('arr', metavar='N', type=int, nargs='+',
                        help='an integer array')
    args = parser.parse_args()
    target = args.arr[-1]
    print(twoSum(args.arr, target))
