import sys

def fizzbuzz(i):
  output = ""
  if i % 3 == 0:
    output += "Fizz"
  if i % 5 == 0:
    output += "Buzz"
  if i % 7 == 0:
    output += "Bazz"
  print("\n- " + output or i)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("\n- Parameter(s) expected.")
    exit(1)
  #print(sys.argv[1:])
  fizzbuzz(int(sys.argv[1]))
