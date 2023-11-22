import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

"""
Given an integer n, return a string array answer (1-indexed) where:
  answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
  answer[i] == "Fizz" if i is divisible by 3.
  answer[i] == "Buzz" if i is divisible by 5.
  answer[i] == i (as a string) if none of the above conditions are true.
Return Value: List[str]
"""
def fizzBuzz(n: int):
    result = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if s == "":
            s += str(i)
        result.append(s)
    return result

print(fizzBuzz(int(sys.argv[1])))