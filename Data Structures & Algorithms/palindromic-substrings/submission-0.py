class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def count(l, r):
            count = 0
            while 0 <= l and r < n and s[l] == s[r]:
                count += 1
                l += -1
                r += 1
            return count
        
        sol = 0
        for i in range(n):
            sol += count(i, i) + count(i, i + 1)

        return sol


        