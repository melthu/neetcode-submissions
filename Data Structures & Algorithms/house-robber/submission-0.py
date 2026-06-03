class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        # G-function
        def G(i):
            # base case:
            if i >= n:
                return 0
            
            if dp[i] == -1:
                dp[i] = max(nums[i] + G(i + 2), G(i + 1))
            return dp[i]
            
        return G(0)
        