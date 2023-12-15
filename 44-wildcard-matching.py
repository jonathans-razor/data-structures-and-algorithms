import sys

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

class Solution:
    def isMatch(self, s: str, pattern: str) -> bool:
        """
        Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
        '?' Matches any single character.
        '*' Matches any sequence of characters (including the empty sequence).
        The matching should cover the entire input string (not partial).
        Return Value: bool
        """
        s_len = len(s)
        pattern_len = len(pattern)
        dp = [[False] * (pattern_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True
        for i in range(1, pattern_len + 1):
            if pattern[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        for i in range(1, s_len + 1):
            for j in range(1, pattern_len + 1):
                if pattern[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] 
                elif pattern[j - 1] == '?' or s[i - 1] == pattern[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[s_len][pattern_len]

if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch(sys.argv[1], sys.argv[2]))