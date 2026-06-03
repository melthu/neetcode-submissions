class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)

        lo = 1
        hi = m
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.valid(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def valid(self, piles, h, k):
        total = 0
        for pile in piles:
            total += (pile + k - 1) // k
        return total <= h
            



        