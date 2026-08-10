class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(start, end):
            dp = [0, 0]
            for i in range(start, end):
                g = max(nums[i] + dp[0], dp[1])
                dp[0] = dp[1]
                dp[1] = g
            return dp[1]

        return max(helper(1, n), helper(0, n-1))

        


        



        
        