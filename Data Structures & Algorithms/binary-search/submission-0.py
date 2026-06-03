class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        lo = 0
        hi = n - 1

        while lo <= hi:
            mi = lo + (hi - lo) // 2
            print(nums[lo], nums[mi], nums[hi])
            if target == nums[mi]:
                return mi
            elif target < nums[mi]:
                hi = mi - 1
            elif target > nums[mi]:
                lo = mi + 1
        return -1

        