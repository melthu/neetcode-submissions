class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        one, two = 0, 0

        for i in range(n):
            curr = max(nums[i] + two, one)
            two = one
            one = curr

        return curr
        