class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def check(l, r):
            while 0 <= l and r < n and s[l] == s[r]:
                l += -1
                r += 1
            return s[l + 1: r]
        
        sol = ""
        for i in range(n):
            o = check(i, i)
            e = check(i, i + 1)
            if len(o) > len(sol):
                sol = o
            if len(e) > len(sol):
                sol = e

        return sol