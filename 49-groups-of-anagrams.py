import sys
from collections import defaultdict

def groupAnagrams(strs):
  """Groups anagrams together.

  Args:
    strs: A list of strings.

  Returns:
    A list of lists of strings, where each sublist contains anagrams.
  """

  groups = defaultdict(list)
  for str in strs:
    sorted_str = ''.join(sorted(str))
    groups[sorted_str].append(str)
  return list(groups.values())

if __name__ == '__main__':
  strs = sys.argv[1:]
  groups = groupAnagrams(strs)
  print(groups)
