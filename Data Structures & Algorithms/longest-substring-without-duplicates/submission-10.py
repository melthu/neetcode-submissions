class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        seen = {}
        sol = 0

        l, r = 0, 0
        while r < n:
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            sol = max(sol, r - l + 1)
            r += 1

        return sol
            
            

        