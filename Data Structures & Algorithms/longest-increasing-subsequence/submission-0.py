class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            idx = n - 1 - i
            for j in range(idx, n):
                if nums[idx] < nums[j]:
                    dp[idx] = max(1 + dp[j], dp[idx])
        return max(dp)

