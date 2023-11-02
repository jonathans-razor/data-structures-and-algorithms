import sys

def findFirstOccurrence(haystack: str, needle: str) -> int:
    if haystack is None or needle is None or needle == "":
        return -1
    if haystack == "" or len(haystack) < len(needle):
        return -1 
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

print(findFirstOccurrence(sys.argv[1], sys.argv[2]))