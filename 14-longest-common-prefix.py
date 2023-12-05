import sys

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

return type: string
"""
def findLongestCommonPrefix(strs):
    answer = ""
    if len(strs) == 0:  
        return answer
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    first = strs[0]
    last = strs[-1]
    for i in range(len(first)):
        if first[i] == last[i]:
            answer += first[i]
        else:
            break
    return answer

if __name__ == "__main__":
    strs = sys.argv[1:]
    longestCommonPrefix = findLongestCommonPrefix(strs)
    print(longestCommonPrefix)