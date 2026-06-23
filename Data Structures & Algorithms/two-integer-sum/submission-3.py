class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # want to be able to do one pass through array
        # and know if for index i, if there's an index j
        # such that nums[j] = target - nums[i]
        n = len(nums)

        c = dict()
        for i in range(n):
            c[target - nums[i]] = i

        for i in range(n):
            if (nums[i] in c) and c[nums[i]] != i:
                return [i, c[nums[i]]]
