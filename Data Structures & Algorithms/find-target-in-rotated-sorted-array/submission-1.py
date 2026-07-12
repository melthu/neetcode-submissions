class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1
        while l < r:
            print(nums[l:r+1])
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            else:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
        if nums[l] == target:
            return l
        else: 
            return -1

        