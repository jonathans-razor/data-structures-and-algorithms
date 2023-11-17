# LeetCode Problem 205: Isomorphic Strings
# Weblink: https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings are isomorphic.
        :param s: First input string
        :param t: Second input string
        :return: True if strings are isomorphic, False otherwise
        """
        mapping = {}  # Dictionary to store character mappings
        if len(s) != len(t):
            return False  # Different lengths cannot be isomorphic

        for i in range(len(s)):
            if s[i] in mapping:
                print(f"Mapping: {mapping}")
                print("si: " + s[i])
                print("ti: " + t[i])
                if mapping[s[i]] != t[i]:
                    return False  # Mismatched mapping
            else:
                if t[i] in mapping.values():
                    return False  # Two characters cannot map to the same character
                mapping[s[i]] = t[i]

        return True

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python isomorphic_strings.py <string1> <string2>")
        sys.exit(1)

    s, t = sys.argv[1], sys.argv[2]
    solution = Solution()
    result = solution.isIsomorphic(s, t)
    print(f"Isomorphic: {result}")