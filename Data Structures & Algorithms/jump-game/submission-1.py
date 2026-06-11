class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        m = 0
        for i in range(n):
            if m < i:
                return False
            m = max(m, i + nums[i])

        return True
        