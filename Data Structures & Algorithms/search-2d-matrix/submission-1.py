class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target < matrix[mid][0]:
                hi = mid - 1
            elif target > matrix[mid][n - 1]:
                lo = mid + 1
            else:
                return self.binarySearch(matrix[mid], target)
        return False

    def binarySearch(self, nums, target):
        n = len(nums)

        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
                    

            
        