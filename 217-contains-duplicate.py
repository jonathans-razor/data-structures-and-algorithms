import argparse

def has_duplicates(arr):
    return len(arr) != len(set(arr))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if an array has duplicates.')
    parser.add_argument('arr', metavar='N', type=int, nargs='+',
                        help='an integer array')
    args = parser.parse_args()
    if has_duplicates(args.arr):
        print('The array contains duplicates.')
    else:
        print('The array does NOT contain duplicates.')