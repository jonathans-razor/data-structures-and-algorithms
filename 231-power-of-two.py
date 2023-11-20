import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

def isPowerOfTwo(n: int) -> bool:
  i = 0
  while 2 ** i <= n:
    if 2 ** i == n:
      return True
    i += 1
  else: 
    return False

print(isPowerOfTwo(int(sys.argv[1])))