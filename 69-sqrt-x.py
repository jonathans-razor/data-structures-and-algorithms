import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

def mySqrt(x: int) -> int:
  if x == 0:
    return 0
  if x == 1:
    return 1
  start = 0
  end = x
  while start <= end:
    middle = (start + end) // 2
    if middle * middle == x:
      return middle
    elif middle * middle < x:
      start = middle + 1
      res = middle
    else:
      end = middle - 1
  return res

print(mySqrt(int(sys.argv[1])))