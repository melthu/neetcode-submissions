class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        sol = nums[0]
        dpmin, dpmax = nums[0], nums[0]
        for i in range(1, n):
            tempmax = max(nums[i] * dpmax, nums[i] * dpmin, nums[i])
            tempmin = min(nums[i] * dpmax, nums[i] * dpmin, nums[i])
            dpmax, dpmin = tempmax, tempmin
            sol = max(dpmax, sol)
        return sol



        