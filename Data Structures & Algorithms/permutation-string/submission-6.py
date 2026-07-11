class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        
        l, r = 0, n - 1
        set1 = Counter(s1)
        set2 = Counter(s2[l : r])
        while r < m:
            set2[s2[r]] = set2.get(s2[r], 0) + 1 
            if set1 == set2:
                return True
            else:
                set2[s2[l]] -= 1
                l += 1
                r += 1
        return False
        
        