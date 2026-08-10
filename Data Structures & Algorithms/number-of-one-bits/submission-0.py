class Solution:
    def hammingWeight(self, n: int) -> int:
        sol = 0
        for i in range(32):
            mask = 1 << i
            if mask & n:
                sol += 1
        return sol
        
        
        