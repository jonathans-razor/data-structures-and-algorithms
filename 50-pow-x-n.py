import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)


class Solution:
    def myPow(self, x: float, n: int) -> int:
        """
        Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
        retrn value: float
        """
        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        return float(f) if n >= 0 else 1 / f

if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(float(sys.argv[1]), int(sys.argv[2])))
