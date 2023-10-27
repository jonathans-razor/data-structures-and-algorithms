import sys

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    charSet = set()
    left = 0
    result = 0
    for r in range(len(s)):    
        while s[r] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[r])
        result = max(result, r - left + 1)
    return result

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

print(lengthOfLongestSubstring(sys.argv[1]))