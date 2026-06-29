class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        sol = 0
        for num in s:
            if num - 1 in s:
                continue
            i = 0
            while num + i in s:
                i += 1
            sol = max(sol, i)
        return sol
            





        return 1
        