class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        l, r = 0, n - 1
        while l <= r:
            if r - l + 1 <= 3:
                return min(nums[l:r+1])

            mid = l + (r - l) // 2
            if nums[l] < nums[mid] and nums[l] > nums[r]:
                l = mid + 1
            else:
                r = mid

            

        