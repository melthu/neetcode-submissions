class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            fewest = float('inf')
            for c in coins:
                if i - c >= 0:
                    fewest = min(dp[i - c], fewest)
            dp[i] = 1 + fewest
        sol = dp[amount]
        if sol == float('inf'):
            return -1
        else:
            return sol
        
        