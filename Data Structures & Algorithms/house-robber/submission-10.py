class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for num in nums:
            g = max(num + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = g
        return dp[1]
        