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
        add = [0] * n
        for i in range(n):
            add[i] = min(l[i], r[i])
            if add[i] - height[i] > 0:
                res += add[i] - height[i]
        print(l)
        print(r)
        print(add)
        return res

            
        