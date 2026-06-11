class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        e = 0
        ne = 0
        c = 0
        for i in range(n-1):
            ne = max(ne, i + nums[i])
            if i == e:
                e = ne
                c += 1
                if e >= n-1:
                    return c
        return c