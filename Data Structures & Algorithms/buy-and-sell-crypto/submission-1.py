class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        l, r = 0, 1
        minL = prices[0]
        sol = 0
        while r < n:
            sol = max(sol, prices[r] - minL)
            if prices[r] < minL:
                minL = prices[r]
                l = r
            r += 1

        return sol




        