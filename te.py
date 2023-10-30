import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

def reverseString(s: str) -> int:
  return s[::-1]

print(reverseString(sys.argv[1]))
