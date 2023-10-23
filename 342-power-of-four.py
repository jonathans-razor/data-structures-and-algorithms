import sys

def isPowerOfFour(num):
  if num == 1:
    return True
  if num % 4 != 0:
    return False
  return isPowerOfFour(num / 4)

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

if __name__ == '__main__':
  userInput = sys.argv[1]
  print(isPowerOfFour(int(userInput)))