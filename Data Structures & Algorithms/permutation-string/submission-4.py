class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)

        if not c1 <= c2:
            return False

        
        print(c1)
        for i in range(2 * len(s2) - len(s1)):
            print(s2[i: i + len(s1)])
            if Counter(s2[i: i + len(s1)]) == c1:
                return True

        return False
        

        