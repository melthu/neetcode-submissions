class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i, sum):
            if i == n:
                if sum == target:
                    res.append(sol[:])
                return
            
            k = (target - sum) // nums[i]
            for j in range(k + 1):
                for _ in range(j):
                    sol.append(nums[i])
                sum += j * nums[i]
                backtrack(i + 1, sum)
                for _ in range(j):
                    sol.pop()
                sum -= j * nums[i]
            return

        backtrack(0, 0)
        return res
            

            




            

        

        