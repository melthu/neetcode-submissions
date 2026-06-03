class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        nums.sort()
        for i in range(n):    # iterate over each target in nums
            target = nums[i]
            j = i + 1
            k = n - 1

            if (i > 0 and target == nums[i - 1]):
                continue

            while (j < k):
                sum = -(nums[j] + nums[k])

                if (sum == target):
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (j < k and nums[j] == nums[j-1]):
                        j += 1
                elif (sum > target):
                    j += 1
                else:
                    k -=1

        return result

    


        