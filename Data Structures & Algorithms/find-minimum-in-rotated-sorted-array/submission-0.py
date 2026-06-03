class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[lo] <= nums[hi]:     # window is sorted -> return lowest value in window
                return nums[lo]
            elif nums[mid] > nums[hi]:  # right half of window is unsorted -> search right
                lo = mid + 1
            else:                       # left half of window unsorted
                hi = mid 
            print(nums[lo], nums[mid], nums[hi])
        
        return nums[lo]