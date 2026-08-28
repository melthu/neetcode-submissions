class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = []
        for i in range(m + 1):
            dp.append([0] * (n + 1))
        
        for i in range(m):
            row = m - 1 - i
            for j in range(n):
                col = n - 1 - j
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

        print(dp)
        return dp[0][0]
        
        


        