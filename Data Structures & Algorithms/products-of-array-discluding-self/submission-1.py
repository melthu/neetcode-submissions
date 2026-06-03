class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [0] * n
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = nums[i] * left[i-1]

        right = [0] * n
        right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right[i] = nums[i] * right[i+1]

        result = [0] * n
        result[0] = right[1]
        result[n-1] = left[n-2]
        for i in range(1, n-1):
            result[i] = left[i-1] * right[i+1]

        return result