import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def isNaturalNumberLessThan5000(x: int) -> int:
  if x.isdigit():
    if int(x) <= 5000:
      return 0
  return 1

print(isNaturalNumberLessThan5000(sys.argv[1]))