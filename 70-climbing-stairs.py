import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    firstWay = 1
    secondWay = 2
    for i in range(3, n + 1):
        thirdWay = firstWay + secondWay
        firstWay = secondWay
        secondWay = thirdWay
    return secondWay  

print(climbStairs(int(sys.argv[1])))