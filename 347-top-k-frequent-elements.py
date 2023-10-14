import collections
import argparse

def k_most_frequent(nums, k):
    counter = collections.Counter(nums)
    return [num for num, _ in counter.most_common(k)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the k most frequent elements in an integer array.")
    parser.add_argument("nums", metavar="N", type=int, nargs="+", help="an integer array")
    parser.add_argument("k", metavar="K", type=int, help="the number of most frequent elements to return")
    args = parser.parse_args()
    print(k_most_frequent(args.nums, args.k))