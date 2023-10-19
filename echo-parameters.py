import sys

def isAnagram(s1: str, s2: str) -> bool: 
  return sorted(s1) == sorted(s2)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    exit(1)
  print(sys.argv[1:])
