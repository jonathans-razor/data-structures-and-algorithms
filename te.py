import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

def r(s: str) -> int:
  #print("- ")
  return s[::-1]

print(r(sys.argv[1]))
