class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make hash table of complements
        complements = dict()
        for i in range(len(nums)):
            complements[target - nums[i]] = i
            
        for i in range(len(nums)):
            if nums[i] in complements and i != complements[nums[i]]:
                return [min(i, complements[nums[i]]), max(i, complements[nums[i]])]


        