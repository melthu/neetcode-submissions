class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        dp.append(True)

        for i in range(n):
            idx = n - 1 - i
            for word in wordDict:
                if s[idx:idx + len(word)] == word and dp[idx + len(word)]:
                    dp[idx] = True
        
        return dp[0]
                
        