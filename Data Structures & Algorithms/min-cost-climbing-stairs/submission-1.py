class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = 0, 0
        
        for i in range(1, n + 1):
            curr = cost[n - i] + min(one, two)
            two = one
            one = curr

        return min(one, two)