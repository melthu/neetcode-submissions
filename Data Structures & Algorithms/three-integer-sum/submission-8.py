class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sol = []
        print(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    sol.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    print(i, l, r)
                    print([nums[i], nums[l], nums[r]])
                if nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return sol

                    
