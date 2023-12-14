import sys

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

def multiply(num1: str, num2: str) -> str:
    '''
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.      
    Return Value:
    '''
    if num1 == "0" or num2 == "0":
        return "0"
    m, n = len(num1), len(num2)
    res = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            multiplied_result = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            sum = multiplied_result + res[p2]
            res[p2] = sum % 10
            res[p1] += sum // 10
    i = 0
    while i < len(res) and res[i] == 0:
        i += 1
    return "".join(map(str, res[i:]))

if __name__ == "__main__":
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    print(multiply(num1, num2))