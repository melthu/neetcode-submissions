class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        res = []

        l, r = 0, k
        while r < n + 1:
            res.append(max(nums[l:r]))
            l += 1
            r += 1

        return res
            



        