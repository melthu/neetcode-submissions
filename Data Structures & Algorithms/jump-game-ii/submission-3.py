class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        e = 0
        ne = 0
        c = 0

        for i in range(n):
            ne = max(ne, i + nums[i])

            if i == e:
                e = ne
                c += 1
                if e >= n-1:
                    return c