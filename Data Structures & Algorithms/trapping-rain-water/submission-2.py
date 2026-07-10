class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        maxL, maxR = 0, 0
        res = 0
        while l <= r:
            if maxL < maxR:
                if min(maxL, maxR) - height[l] > 0:
                    res += min(maxL, maxR) - height[l]
                maxL = max(maxL, height[l])
                l += 1
            else:
                if min(maxL, maxR) - height[r] > 0:
                    res += min(maxL, maxR) - height[r]
                maxR = max(maxR, height[r])
                r -= 1

        return res

