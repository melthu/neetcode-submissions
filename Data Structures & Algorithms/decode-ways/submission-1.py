class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1, 1]
        for i in range(n):
            idx = n - 1 - i
            G = 0
            if 0 < int(s[idx]) < 10:
                G += dp[0]
            if idx + 1 < n and 10 <= int(s[idx:idx + 2]) <= 26:
                G += dp[1]
            dp[1] = dp[0]
            dp[0] = G
        return dp[0]

        