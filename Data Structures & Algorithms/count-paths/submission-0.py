class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] + [0] * (n - 1)
        for i in range(m):
            prev = 0
            for j in range(n):
                dp[j] = dp[j] + prev
                prev = dp[j]
        return dp[n - 1]
            





        