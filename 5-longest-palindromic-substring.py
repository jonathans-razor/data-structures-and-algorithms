import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

"""
Given a string s, return the longest palindromic substring in s.
Return Value: string
"""
def longestPalindromicSubstring(s: str) -> str:
    if len(s) < 2:
        return s
    if s == s[::-1]:
        return s
    lengthOfS = len(s)
    longestSubstring = s[0]
    for i in range(lengthOfS):
        for j in range(i+1, lengthOfS):
            # if the length of the longest substring is greater than the length of the current substring, then there is no need to check the current substring
            if len(longestSubstring) >= j-i+1:
                continue 
            # if the current substring is a palindrome, then check if it is the longest palindrome substring. If it is, then update the longest substring.
            if s[i:j+1] == s[i:j+1][::-1]:
                longestSubstring = s[i:j+1]
    return longestSubstring

print(longestPalindromicSubstring(sys.argv[1]))