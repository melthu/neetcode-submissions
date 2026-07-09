class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = [0] * n, [0] * n
        m = 0
        for i in range(1, n):
            m = max(m, height[i - 1])
            l[i] = m

        m = 0
        for i in range(1, n):
            m = max(m, height[n - i])
            r[n - i - 1] = m

        res = 0
        for i in range(n):
            add = min(l[i], r[i])
            if add - height[i] > 0:
                res += add - height[i]

        return res
