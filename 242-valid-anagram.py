import sys

def isAnagram(s1: str, s2: str) -> bool: 
  #Given two strings s and t, return true if t is an anagram of s, and false otherwise.
  return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide two strings as command line arguments.")
    else:
        s1 = sys.argv[1]
        s2 = sys.argv[2]
        if isAnagram(s1, s2):
            print(f"{s1} and {s2} are anagrams of each other.")
        else:
            print(f"{s1} and {s2} are NOT anagrams of each other.")
