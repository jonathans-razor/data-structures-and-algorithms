import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

'''

Return Value:
'''
def x(s: str) -> int:
  return s[::-1]

print(x(sys.argv[1]))
