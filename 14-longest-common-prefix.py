import sys
from collections import defaultdict

def findLongestCommonPrefix(strs):
  answer = ""
  sortedListOfStrings = sorted(strs)
  firstWord = sortedListOfStrings[0]
  lastWord = sortedListOfStrings[-1]
  print("fw: " + firstWord, "lw: " + lastWord)
  print("1w: " + str(len(firstWord)))
  length = min(len(firstWord), len(lastWord))
  print("length: " + str(length))
  for i in range(min(len(firstWord), len(lastWord))):
    if(firstWord[i] != lastWord[i]):
      return answer
    answer += firstWord[i]
  return answer

if __name__ == '__main__':
  strs = sys.argv[1:]
  longestCommonPrefix = findLongestCommonPrefix(strs)
  print(longestCommonPrefix)
