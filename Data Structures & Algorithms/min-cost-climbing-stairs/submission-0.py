class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n
        
        def G(i):
            # base case:
            if i == n:
                return 0
            if i > n:
                return float('inf')

            if dp[i] != -1:
                return dp[i]

            dp[i] = cost[i] + min(G(i + 1), G(i + 2))
            return dp[i]

        return min(G(0), G(1))
        
        