class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [1]

        left = [1] * n
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = nums[i] * left[i - 1]

        right = [1] * n
        right[n - 1] = nums[n - 1]
        for i in range(2, n + 1):
            right[n - i] = nums[n - i] * right[n - i + 1]

        print(left)
        print(right)
        sol = [1] * n
        sol[0] = right[1]
        sol[n - 1] = left[n - 2]
        for i in range(1, n - 1):
            sol[i] = left[i - 1] * right[i + 1]

        return sol


        
