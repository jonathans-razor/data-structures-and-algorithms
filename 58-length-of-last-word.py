import sys

def lengthOfLastWord(s: str) -> int:
  if(len(s) == 0):
    return 0
  words = s.split()
  if(len(words) == 0):
    return 0
  return len(words[-1])

if __name__ == '__main__':
  print(lengthOfLastWord(sys.argv[1]))