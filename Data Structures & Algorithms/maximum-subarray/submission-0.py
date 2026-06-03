class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if sum so far is positive keep it, if negative start new
        max = float('-inf')
        sum = 0

        for num in nums:
            sum += num;
            if sum > max:
                max = sum

            if sum < 0:
                sum = 0
        
        return max
        