import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        A valid number can be split up into these components (in order):

        A decimal number or an integer.
        (Optional) An 'e' or 'E', followed by an integer.
        A decimal number can be split up into these components (in order):

        (Optional) A sign character (either '+' or '-').
        One of the following formats:
        One or more digits, followed by a dot '.'.
        One or more digits, followed by a dot '.', followed by one or more digits.
        A dot '.', followed by one or more digits.
        An integer can be split up into these components (in order):

        (Optional) A sign character (either '+' or '-').
        One or more digits.
        For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

        Given a string s, return true if s is a valid number.



        Example 1:

        Input: s = "0"
        Output: true
        Example 2:

        Input: s = "e"
        Output: false
        Example 3:

        Input: s = "."
        Output: false


        Constraints:

        1 <= s.length <= 20
        s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'
        return value: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False

        def isInteger(s: str, signed: bool) -> bool:
            if len(s) == 0:
                return False

            if signed and (s[0] == '+' or s[0] == '-'):
                s = s[1:]

            if len(s) == 0:
                return False

            for c in s:
                if not c.isdigit():
                    return False
            return True

        def isDecimal(s: str, signed: bool) -> bool:
            if len(s) == 0:
                return False

            if signed and (s[0] == '+' or s[0] == '-'):
                s = s[1:]

            if len(s) == 0:
                return False

            if s.find('.') == -1:
                return False

            parts = s.split('.')
            if len(parts) != 2:
                return False

            if len(parts[0]) == 0 and len(parts[1]) == 0:
                return False

            if len(parts[0]) > 0 and not isInteger(parts[0], False):
                return False

            if len(parts[1]) > 0 and not isInteger(parts[1], False):
                return False

            return True

        def isScientific(s: str) -> bool:
            if len(s) == 0:
                return False

            if s.find('e') == -1 and s.find('E') == -1:
                return False

            parts = None
            if s.find('e') != -1:
                parts = s.split('e')
            else:
                parts = s.split('E')

            if len(parts) != 2:
                return False

            if len(parts[0]) == 0 or len(parts[1]) == 0:
                return False

            if not isDecimal(parts[0], True) and not isInteger(parts[0], True):
                return False

            if not isInteger(parts[1], True):
                return False

            return True

        if isInteger(s, True) or isDecimal(s, True) or isScientific(s):
            return True

        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isNumber(sys.argv[1]))