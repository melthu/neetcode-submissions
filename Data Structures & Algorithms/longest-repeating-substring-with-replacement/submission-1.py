class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        count = {}
        maxf = 0
        sol = 0

        l, r = 0, 0
        while r < n:
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            if (r - l + 1) - maxf > k: # if not valid or would not change result
                count[s[l]] -= 1
                l += 1
            sol = max(sol, r - l + 1)
            r += 1
        return sol



            



            
            


        